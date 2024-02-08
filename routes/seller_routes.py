import os
from fastapi import APIRouter
from pymongo import MongoClient
from controllers.seller_controller import seller_controller
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()
client = AsyncIOMotorClient(os.environ.get("MONGO_DB_URL"))

# router = APIRouter()
# seller_controller = seller_controller()

class seller_routes:
    def __init__(self):
        self.__router = APIRouter()
        self.__seller_controller = seller_controller(client)
        self.config_routes()
        
    def config_routes(self):
        self.__router.add_api_route("/", self.__seller_controller.get_all_sellers, methods=["GET"])
        self.__router.add_api_route("/generate_new_seller_ID", self.__seller_controller.generate_new_seller_id, methods=["GET"])
        self.__router.add_api_route("/", self.__seller_controller.create_seller, methods=["POST"])
        self.__router.add_api_route("/", self.__seller_controller.update_seller, methods=["PUT"])
        self.__router.add_api_route("/{seller_id}", self.__seller_controller.delete_seller, methods=["DELETE"])
        self.__router.add_api_route("/get_by_seller_id/{seller_id}", self.__seller_controller.get_seller_by_seller_id, methods=["GET"])
        self.__router.add_api_route("/get_by_seller_contact/{seller_contact}", self.__seller_controller.get_seller_by_seller_contact, methods=["GET"])
        
    def get_router(self):
        return self.__router