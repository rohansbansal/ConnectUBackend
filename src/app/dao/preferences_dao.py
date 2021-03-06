from app.utils.db_instance import mongo
from flask_pymongo import ObjectId


def find_preferences_by_id(user_id):
    query = {"_id": user_id}
    return mongo.db.preferences.find_one(query)


def create_preference(user_id, general, clubs, sports, entertainment, music, movies):
    preference = {
        "_id": user_id,
        "general": general,
        "clubs": clubs,
        "sports": sports,
        "entertainment": entertainment,
        "music": music,
        "movies": movies,
    }
    return (mongo.db.preferences.insert_one(preference), str(user_id))