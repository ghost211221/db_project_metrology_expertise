# Converts a docx file with tables and images to (simple) HTML
# ORIGINAL CODE BY DAVID SSALI AT SOURCE: https://medium.com/@dvdssali/docx-to-html-1374eb6491a1
#
# Requires the Python module 'python-docx' <https://python-docx.readthedocs.io>
#
# Example use:
# >>> s = convert('./SOURCEDIR', 'SAMPLE.docx')
# >>> print(s)
# or
# $ python .\convert-docx-to-html.py > temp.html


"""
Конвертер работает. Выдает html документа.
Доработки:
1. сделать выборку стилей параграфов в словарь - из словаря генерить строку css;
2. сделать выборку стилей таблиц в словарь - из словаря генерить строку css;
3. сделать выборку стилей ячеек таблицы в словарь - из словаря генерить строку css;
4. настроить генерацию отступов для вложенных тэгов;
5. перевести определение размеров на pt, как в word.
"""

from docx import Document
from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph
from simplify_docx import simplify
import xml.etree.ElementTree as ET
import time
import re
import os

class Docx2HtmlConverter():

    def __init__(self):

        self.document = None
        self.image_path = ''

        self.list_items = []

        self.page = 1
        self.firstPage = True
        self.paragraph = 1

        self.table_n = 0

        self.body = f'<div class="page page-{self.page}" style="width: 975px;">\n'

        self.body_json = []

        self.__addNewPage()


    def convert(self, dir_path, file):
        """
            dir_path = "./SOURCEDIR"
            file = "SAMPLE.docx"

            image_path will be a directory to store image files; if the directory does not exist it will be created
        """
        splitname = re.split('[. ]', file)
        if len(splitname) > 2:
            self.image_path =  ''.join(splitname[:2]) + '-images'
        else:
            self.image_path = splitname[0] + '-images'

        if not os.path.isdir(self.image_path):
            os.mkdir(self.image_path)

        self.document = Document(dir_path + file)

        self.__covertDocument()

    def getHtml(self):
        """ возврат сгенеренного html кода """

        return self.body

    def getJSON(self):
        """ возврат сгенеренного JSON """

        return self.body_json

    def __covertDocument(self):
        for block in self.__iter_block_items(self.document):
            if isinstance(block, Paragraph):
                self.__detectPageBreakBlock(block)
                tmp_heading_type = self.__get_heading_type(block)

                if re.match("List\sParagraph", tmp_heading_type):
                    self.list_items.append('<li ref="target">' + block.text + '</li>\n')

                elif not block.text.strip():
                    # переводим пустые строку документа в пустые строки
                    self.list_items.append("<br/>\n")

                else:
                    images = self.__render_image(self.document, block, self.image_path, self.image_path)
                    if len(self.list_items) > 0:
                        self.body += self.__render_list_items(self.list_items)
                        self.list_items = []

                    if len(images) > 0:
                        self.body += images

                    else:
                        # modified to use a different outer_tag if a 'Heading' style is found in the original paragraph
                        if 'Heading' in tmp_heading_type:
                            outer_tag = 'h' + tmp_heading_type.split(' ')[-1]

                        else:
                            outer_tag = 'p'
                        self.body += self.__render_runs(block, outer_tag)

            elif isinstance(block, Table):
                self.body += self.__render_table(block, self.document)

        self.body += '</div>\n'

    def __iter_block_items(self, parent):
        """
        Generate a reference to each paragraph and table child within *parent*,
        in document order. Each returned value is an instance of either Table or
        Paragraph. *parent* would most commonly be a reference to a main
        Document object, but also works for a _Cell object, which itself can
        contain paragraphs and tables.
        """
        if isinstance(parent, _Document):
            parent_elm = parent.element.body
        elif isinstance(parent, _Cell):
            parent_elm = parent._tc
        else:
            raise ValueError("something's not right")
        for child in parent_elm.iterchildren():
            if isinstance(child, CT_P):
                yield Paragraph(child, parent)
            elif isinstance(child, CT_Tbl):
                yield Table(child, parent)

    def __detectPageBreakBlock(self, block, blockType='paragraph'):
        """ поиск разрыва страницы в блоке """
        if blockType == 'paragraph':
            for run in block.runs:
                self.__detectPageBreak(run, blockType='paragraph')

        elif blockType == 'table':
            self.__detectPageBreak(block, blockType='table')

        else:
            raise Exception(f"""Page break detector
                unexpected block type - {blockType}""")

    def __detectPageBreak(self, block, blockType='paragraph'):
        """ поиск разрыва строки в Paragraph run или в table row"""
        # if 'lastRenderedPageBreak' in block._element.xml or 'w:br' in block._element.xml and 'type="page"' in block._element.xml:
        if 'w:br' in block._element.xml and 'type="page"' in block._element.xml:
            self.page += 1
            self.__addNewPage()
            self.paragraph = 1
            if blockType == 'paragraph':
                self.body += f'</div>\n<div class="page page-{self.page}" style="width: 975px;">\n'
            else:
                self.body += f'<\ttbody>\n</div>\n<div class="page page-{self.page}" style="width: 975px;">\t<table>\n\t<tbody>\n'

    def __get_heading_type(self, block):
        return block.style.name

    def __render_image(self, document, par, dir_path, book_id):
        # get all of the images in a paragraph 
        # :param par: a paragraph object from docx
        # :return: a list of r:embed 
        
        ids = []
        root = ET.fromstring(par._p.xml)
        namespace = {
                 'a':"http://schemas.openxmlformats.org/drawingml/2006/main", \
                 'r':"http://schemas.openxmlformats.org/officeDocument/2006/relationships", \
                 'wp':"http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"}
        inlines = root.findall('.//wp:inline',namespace)
        for inline in inlines:
            imgs = inline.findall('.//a:blip', namespace)
            for img in imgs:     
                id = img.attrib['{{{0}}}embed'.format(namespace['r'])]
                ids.append(id)
        inlines = root.findall('.//wp:anchor',namespace)
        for inline in inlines:
            imgs = inline.findall('.//a:blip', namespace)
            for img in imgs:     
                id = img.attrib['{{{0}}}embed'.format(namespace['r'])]
                ids.append(id)
        response = ""
        if len(ids) > 0:
            for id in ids:
                image_part = document.part.related_parts[id]
                millis = int(round(time.time() * 1000))
                file_name = str(id) + "-" + str(book_id) + "-" + str(millis) + ".png"
                fr = open(dir_path + "/" + file_name, "wb")
                fr.write(image_part._blob)
                fr.close()
                response += "\t<img border='1' src='" + dir_path + "/" + file_name + "' class='img-responsive'/>\n"
        return response

    def __render_list_items(self, items):
        html = '\t<ul ref="target">\n'
        for item in items:
            html += f'\t\t{item}'

        html += "\t</ul>\n"

        return html

    
    def __render_runs(self, block, outer_tag='p'):
        """ Modified to use a different outer_tag if a 'Heading' style is found in the original paragraph """
        html = "\t<" + outer_tag + ' style="max-width: 975px" ref="target">\n'

        text_ = ''
        for text in block.text.splitlines():
            if 'w:jc' in block._element.xml and 'val="center"'  in block._element.xml:
                html += f'\t\t<center>{text}</center>'
            else:
                html += f'\t\t{text}'
                
            text_ += text

        html += "\t</" + outer_tag + ">\n"
        self.__addPToPage(text_)

        return html

    
    def __render_table(self, block, document):
        """ Modified to treat cell content as a set of blocks to process  """
        table = block

        html = ''
        css = ''
        with open('xml.txt', 'a', encoding='utf8') as f:
            f.write(table._element.xml)
        if self.__has_borders(block):
            css += 'border-spacing: 0px;'
            html = f'\t<table class="table table-bordered" border="1" style="{css}" ref="target">\n'
        else:
            html = f'\t<table class="table" style="{css}">\n'

        for row in table.rows:
            self.__detectPageBreakBlock(block, blockType='table')
            html += '\t\t<tr ref="target">\n'
            for cell in row.cells:
                html += "\t\t\t<td>\n"
                # --- 
                cbody = ""
                clist_items = []
                for cblock in self.__iter_block_items(cell):
                    if isinstance(cblock, Paragraph):
                        tmp_heading_type = self.__get_heading_type(cblock)
                        if re.match("List\sParagraph", tmp_heading_type):
                            clist_items.append('\t\t\t\t<li ref="target">' + cblock.text + "</li>\n")
                        
                        else:
                            images = self.__render_image(document, cblock, self.image_path,self.image_path)
                            if len(clist_items) > 0:
                                cbody += self.__render_list_items(clist_items)
                                clist_items = []

                            if len(images) > 0:
                                cbody = cbody + images

                            else:
                                cbody += self.__render_runs(cblock)

                    elif isinstance(cblock, Table):
                        cbody += self.__render_table(cblock, document, self.image_path)
                
                html += cbody + " "
                html += "\t\t\t</td>\n"

            html += "\t\t</tr>\n"

        html += "\t</table>\n"

        return html

    def __has_borders(self, block):
        return 'w:tcBorders' in block._element.xml

    def __get_block_style(self, block):
        css = ''

        styles = block.style
        print(styles)

        return css

    def __addNewPage(self):
        self.body_json.append(
            {
                'type': 'div',
                'class': f'page page-{self.page}',
                'ref': f'page-{self.page}',
                'style': 'width: 975px',
                'children': []
            }
        )

    def __addPToPage(self, text):
        self.body_json[self.page-1]['children'].append(
            {
                'type': 'p',
                'class': f'paragraph paragraph-{self.paragraph}',                
                'ref': f'page-{self.page}-paragraph-{self.paragraph}',
                'style': '',
                'text': text
            }
        )

        self.paragraph += 1

# if __name__ == '__main__':

    
#     converter = Docx2HtmlConverter()

#     converter.convert('D:\\design\\GeekBrains\\group_project\\db_project_metrology_expertise\\file_storage\\upload\\common\\', 'common__init_document.docx')
#     s = converter.getHtml()

#     with open('text.html', 'w', encoding='utf8') as f:
#         f.write(s)
        
class Docx2JSONConverter():

    def __init__(self):

        self.document = None

        self.body = {}

    def convert(self, dir_path, file):

        self.document = Document(dir_path + file)

        self.__covertDocument()

    def getHtml(self):
        """ возврат сгенеренного html кода """

        return self.body

    def __covertDocument(self):

        self.body = simplify(
            self.document, 
            {
                "ignore-empty-paragraphs": False,
                "ignore-empty-text": False,
                "remove-leading-white-space": False,
            }
        )

if __name__ == '__main__':

    # # read in a document 
    # my_doc = docx.Document('D:\\design\\GeekBrains\\group_project\\db_project_metrology_expertise\\files\\init_document.docx')

    # # coerce to JSON using the standard options
    # my_doc_as_json = simplify(my_doc)

    # # or with non-standard options
    # # my_doc_as_json = simplify(my_doc,{"remove-leading-white-space":False})

    import pprint

    pp = pprint.PrettyPrinter(indent=4)

    converter = Docx2HtmlConverter()

    converter.convert('D:\\design\\GeekBrains\\group_project\\db_project_metrology_expertise\\files\\', 'init_document.docx')

    pp.pprint(converter.getJSON())
    
    