from app.utils.db_instance import mongo
from flask_pymongo import ObjectId


def find_user_by_attributes(**kwargs):
    query = {}
    for attr, value in kwargs.items():
        query[attr] = value
    return mongo.db.users.find_one(query)


def find_user_by_id(user_id):
    query = {"_id": ObjectId(user_id)}
    return mongo.db.users.find_one(query)


def create_user(name, email, major, school, class_year):
    user_id = ObjectId()
    user = {
        "_id": user_id,
        "name": name,
        "email": email,
        "major": major,
        "school": school,
        "class_year": class_year,
    }
    print(mongo.db)
    return (mongo.db.users.insert_one(user), str(user_id))
