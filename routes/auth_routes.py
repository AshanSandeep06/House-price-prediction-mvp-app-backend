import os
from fastapi import APIRouter
from pymongo import MongoClient
from controllers.auth_controller import auth_controller
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()
client = AsyncIOMotorClient(os.environ.get("MONGO_DB_URL"))

class auth_routes:
    def __init__(self):
        self.__router = APIRouter()
        self.__auth_controller = auth_controller(client)
        self.config_routes()
        
    def config_routes(self):
        self.__router.add_api_route("/signup", self.__auth_controller.auth_signup, methods=["POST"])
        self.__router.add_api_route("/login", self.__auth_controller.auth_login, methods=["POST"])
        
    def get_router(self):
        return self.__router