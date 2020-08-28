from app.utils.db_instance import mongo
from flask_pymongo import ObjectId

def create_preference(user_id, general, clubs, sports, entertainment, music, movies):
    preference = {
        "user_id": user_id,
        "general": general,
        "clubs": clubs,
        "sports": sports,
        "entertainment": entertainment,
        "music": music,
        "movies": movies
    }
    print(mongo.db)
    return (mongo.db.preferences.insert_one(preference), str(user_id))