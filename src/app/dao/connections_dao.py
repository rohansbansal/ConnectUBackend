from app.utils.db_instance import mongo
from flask_pymongo import ObjectId


def get_connections_by_id(user_id):
    query = {"_id": user_id}
    return mongo.db.connections.find_one(query)


def upload_connections(user_id, connections):
    key = {"_id": user_id}
    data = {"$set": {"connections": connections}}
    return (mongo.db.connections.update(key, data, upsert=True), str(user_id))
