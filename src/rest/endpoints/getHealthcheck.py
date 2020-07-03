from flask_restful import Resource

import json

class GetHealthcheck(Resource):
    """Endpoint для запроса библиотек

    Extends:
    	Resource
    """
    def get(self):
    	# pass
        return {"status": 200}
