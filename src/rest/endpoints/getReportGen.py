import json
import os
import sys

from flask import send_from_directory, send_file
from flask_restful import Resource, reqparse, request
from sqlalchemy.orm import sessionmaker

from models import DiffJson
from docxHandle.generator import ResultTableGenerator

class GetReportGen(Resource):
    """ endpont для загрузки файла от клиента """

    def __init__(self, **kwargs):
        self.engine  = kwargs['engine']
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.report_generator = ResultTableGenerator()

    def __parseArgs(self, argsList):
        parser = reqparse.RequestParser()
        print(parser)
        for argExp in argsList:
            parser.add_argument(argExp[0], type=argExp[1])
        return parser.parse_args()

    def post(self): 

        # args = self.__parseArgs([('document_id', int),])
        args = request.get_json(force=True)
        print(args)
        if args['data'] and args['data']['document_id']:
            print(args['data']['document_id'])
            print(type(args['data']['document_id']))
            path, name = self.report_generator.generateTable(self.session, args['data']['document_id'])
            print(path, name)
            # return send_file(os.path.join(path, name), as_attachment=True, attachment_filename=name)
            return send_from_directory(path, name, as_attachment=True)

        # if request.form['data']:

        #     diff_data = json.loads(request.form['data'])

        #     path, name = self.report_generator.generateTable(self.session, diff_data['document_id'])

        #     print(path, name)

        #     # return send_file(os.path.join(path, name), as_attachment=True, attachment_filename=name)

        #     return send_from_directory(path, name, as_attachment=True)

