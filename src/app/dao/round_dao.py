from app.utils.db_instance import mongo
from flask_pymongo import ObjectId

def find_round_by_id(uid):
    query = {"_id": uid}
    return mongo.db.round.find_one(query)

def find_round_pairing_by_id(uid):
    query = {"_id": uid}
    return mongo.db.round_pairing.find_one(query)

def create_round(object_id, opted, meet_type, first_time):
    round = {
        "_id": object_id,
        "opted": opted,
        "meet_type": meet_type,
        "first_time": first_time
    }
    return (mongo.db.round.insert_one(round), str(_id))

def create_round_pairing(user_id, emails):
    round_pairing = {
        "_id": user_id,
        "pairing": emails
    }
    return (mongo.db.round_pairing.insert_one(round_pairing), str(user_id))