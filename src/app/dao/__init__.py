from app.utils.db_instance import mongo
from bson.objectid import ObjectId
from flask import request
from pymongo import ReturnDocument, ASCENDING, DESCENDING
from os import environ
import requests
