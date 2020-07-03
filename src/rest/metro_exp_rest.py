import os

import hashlib

from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask_cors import CORS

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from endpoints.getHealthcheck import GetHealthcheck


ROOTDIR = os.path.dirname(os.path.abspath(__file__))

engine  = create_engine('sqlite:///%s' % (ROOTDIR + '/metro_rest.db'), 
    echo=False)#, pool_recycle=280)

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)
api = Api(app)

CORS(app)


api.add_resource(GetHealthcheck, '/healthcheck')

# @app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')