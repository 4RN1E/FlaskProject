from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

MONGO_USERNAME = os.environ.get("MONGO_USERNAME")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")
MONGO_CLUSTER_URL = os.environ.get("MONGO_CLUSTER_URL")

print(MONGO_CLUSTER_URL)