import json
import os
import sys

from flask_restful import Resource, reqparse, request
from werkzeug.utils import secure_filename

sys.path.insert(0, '..\\')

from config import ALLOWED_EXTENSIONS, FILE_STORAGE_PATH

class GetFileUpload(Resource):
    """ endpont для загрузки файла от клиента """

    def __init__(self, **kwargs):
        self.engine  = kwargs['engine']

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
            filename = secure_filename(file.filename)
            file.save(os.path.join(FILE_STORAGE_PATH, 'upload\\common', filename))
