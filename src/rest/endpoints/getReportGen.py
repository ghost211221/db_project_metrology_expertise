import json
import os
import sys

from flask import send_from_directory, send_file
from flask_restful import Resource, reqparse, request

from models import DiffJson
from docxHandle.generator import ResultTableGenerator

class GetReportGen(Resource):
    """ endpont для загрузки файла от клиента """

    def __init__(self, **kwargs):
        self.session  = kwargs['session']

        self.report_generator = ResultTableGenerator()

    def __parseArgs(self, argsList):
        parser = reqparse.RequestParser()
        for argExp in argsList:
            parser.add_argument(argExp[0], type=argExp[1])
        return parser.parse_args()

    def post(self): 
        args = request.get_json(force=True)
        if args['data'] and args['data']['document_id']:
            path, name = self.report_generator.generateTable(self.session, args['data']['document_id'])

            return send_from_directory(path, name, as_attachment=True)
