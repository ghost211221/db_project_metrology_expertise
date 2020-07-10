import json
import re
import os

from docx import Document

from sqlalchemy.orm import sessionmaker
from models import InitDocumentJson, DiffJson

class ResultTableGenerator():
    """ Класс генератора сводной таблицы
    
    [description]
    """

    def __init__(self):
        self.doc = Document()

        self.file_name = ''

        self.db_session = None
        self.document_id = None
        self.diffs = []
        self.diffs_cnt = 0

    def generateTable(self, db_session, document_id):
        """ генерация таблицы"""
        self.document_id = document_id
        self.db_session = db_session

    def __getDiffs(self):
        diffs = self.db_session.query(DiffJson).filter_by(init_json_id=self.document_id)
        self.diffs = diffs.all()
        self.diffs_cnt = diffs.count()

    def __getFileName(self):
        self.file_name = self.db_session.query(UploadFiles).filter_by(id=self.document_id).first().name

    def __generate(self):
        """добавляем таблицу 4 на хз"""

        table = doc.add_table(rows = self.diffs_cnt+1, cols = 4)
        # применяем стиль для таблицы
        table.style = 'Table Grid'

        # заполняем таблицу данными
        for row in range(self.diffs_cnt+1):
            if row > 0:
                diff = diffs[row-1]
            for col in range(4):
                # получаем ячейку таблицы
                cell = table.cell(row, col)
                # записываем в ячейку данные
                if row == 0:
                    cell.text = 'Местоположение'
                    cell.text = 'Исходный текст'
                    cell.text = 'Исправление'
                    cell.text = 'Комментарий'

                else:
                    if col == 0:
                        idxClass = re.search(r'[A-Za-z\-0-9]+', diff['firstEl'])
                        cell.text = idxClass

                    elif col == 1:
                        cell.text = diff['initText']

                    elif col == 2:
                        cell.text = diff['editText']

        file_name_list = self.file_name.split('.')

        filename = '.'.join(file_name_list[0] + '__table', file_name_list[1])
        filepath = os.path.join(FILE_STORAGE_PATH, 'download\\common\\')

        doc.save(os.path.join(FILE_STORAGE_PATH, 'download\\common\\', filename))