from bson import objectid
from datetime import datetime
import json


class MongoEncoder(json.JSONEncoder):
    def default(self, val):
        if isinstance(val, datetime):
            return val.isoformat()
        elif isinstance(val, objectid.ObjectId):
            return str(val)
        return json.JSONEncoder.default(self, val)
