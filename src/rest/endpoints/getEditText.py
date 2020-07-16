import json
import os
import sys

from flask_restful import Resource, reqparse, request
from werkzeug.utils import secure_filename
from sqlalchemy.orm import sessionmaker
from models import InitDocumentJson, DiffJson

class GetEditText(Resource):
    """ endpont для загрузки файла от клиента """

    def __init__(self, **kwargs):
        self.session  = kwargs['session']
        
    def __parseArgs(self, argsList):
        parser = reqparse.RequestParser()
        for argExp in argsList:
            parser.add_argument(argExp[0], type=argExp[1])
        return parser.parse_args()

    def post(self): 
        if request.form['data']:
            diff_data = json.loads(request.form['data'])

            init_doc = self.session.query(InitDocumentJson).filter_by(init_file_id=int(diff_data['document_id'])).first()
            if init_doc:
                diff_ = self.session.query(DiffJson).filter_by(json=json.dumps(diff_data), init_json_id=init_doc.id).first()
                if not diff_:
                    diff_ = DiffJson(json=json.dumps(diff_data), init_json_id=init_doc.id)
                    self.session.add(diff_)
                    self.session.commit()

