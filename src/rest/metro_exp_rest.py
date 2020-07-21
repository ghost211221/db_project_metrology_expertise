#!/home/ghost/design/programming/python/geekbrains/group_project/expenv/bin/python3.7

import os

import hashlib

from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask_cors import CORS

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

from endpoints.getHealthcheck import GetHealthcheck
from endpoints.getFileUpload import GetFileUpload
from endpoints.getEditText import GetEditText
from endpoints.getReportGen import GetReportGen


ROOTDIR = os.path.dirname(os.path.abspath(__file__))

engine  = create_engine('sqlite:///%s' % (ROOTDIR + '/metro_rest.db'), 
    echo=False)#, pool_recycle=280)

Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

app = Flask(__name__)
api = Api(app)

CORS(app)


api.add_resource(GetHealthcheck, '/healthcheck')

api.add_resource(GetFileUpload, '/file-upload', resource_class_kwargs={
        "session": session
    }
)
api.add_resource(GetEditText, '/text-edited', resource_class_kwargs={
        "session": session
    }
)
api.add_resource(GetReportGen, '/report-gen', resource_class_kwargs={
        "session": session
    }
)

# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
#     response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'
#     return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')