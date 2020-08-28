from app.utils.db_instance import mongo
from flask_pymongo import ObjectId


def get_pairings_by_id(user_id):
    query = {"_id": user_id}
    return mongo.db.pairings.find_one(query)


def update_pairings(user_id, pairings):
    key = {"_id": user_id}
    data = {"$set": {"pairings": pairings}}
    return (mongo.db.pairings.update(key, data, upsert=True), str(user_id))
