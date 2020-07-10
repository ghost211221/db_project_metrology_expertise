import json
import os
import sys

from flask_restful import Resource, reqparse, request
from werkzeug.utils import secure_filename
from sqlalchemy.orm import sessionmaker

from config import ALLOWED_EXTENSIONS, FILE_STORAGE_PATH
from models import UploadFiles, InitDocumentJson

from docxHandle.converter import Docx2HtmlConverter

class GetFileUpload(Resource):
    """ endpont для загрузки файла от клиента """

    def __init__(self, **kwargs):
        self.engine  = kwargs['engine']
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.converter = Docx2HtmlConverter()

    def __allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    def __parseArgs(self, argsList):
        parser = reqparse.RequestParser()
        for argExp in argsList:
            parser.add_argument(argExp[0], type=argExp[1])
        return parser.parse_args()

    def post(self): 
        """ получение файла от клиента, сохранение в БД, преобразование в HTML, отправка HTML клиенту
            потом нужно будет прикрутить шифрование
        """
        file = request.files['file']
        if file and self.__allowed_file(file.filename):
            filename = f'common__{secure_filename(file.filename)}'
            filepath = os.path.join(FILE_STORAGE_PATH, 'upload\\common\\')
            file.save(os.path.join(FILE_STORAGE_PATH, 'upload\\common\\', filename))

            file_ = self.session.query(UploadFiles).filter_by(name=filename, path=filepath).first()
            if not file_:
                file_ = UploadFiles(name=filename, path=filepath)
                self.session.add(file_)
                self.session.commit()
                
            self.converter.convert(file_.path, file_.name)

            json_data = self.converter.getJSON()

            print(file_.id)

            json_ = self.session.query(InitDocumentJson).filter_by(json=json.dumps(json_data), init_file_id=file_.id).first()
            if not json_:
                json_ = InitDocumentJson(
                    json=json.dumps(json_data),
                    init_file_id=file_.id
                )
                self.session.add(json_)
                self.session.commit()

            self.session.commit()

            return {'document_id': file_.id, 'data': json_data}

