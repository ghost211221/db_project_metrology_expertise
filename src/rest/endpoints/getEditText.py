import json
import os
import sys

from flask_restful import Resource, reqparse, request
from werkzeug.utils import secure_filename
from sqlalchemy.orm import sessionmaker
from models import UploadFiles

class GetEditText(Resource):
    """ endpont для загрузки файла от клиента """

    def __init__(self, **kwargs):
        self.engine  = kwargs['engine']
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def __parseArgs(self, argsList):
        parser = reqparse.RequestParser()
        for argExp in argsList:
            parser.add_argument(argExp[0], type=argExp[1])
        return parser.parse_args()

    def post(self): 
        """ получение файла от клиента, сохранение в БД, преобразование в HTML, отправка HTML клиенту
            потом нужно будет прикрутить шифрование
        """
        print(request)
        # print(request.values)
        print(request.form)
        # print(request.args)
        # print(request.data)
        # print(request.json)
        # [print(k,v) for k,v in request.__dict__.items()]
