import os
from fastapi import APIRouter
from pymongo import MongoClient
from controllers.selling_house_controller import selling_house_controller
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()
client = AsyncIOMotorClient(os.environ.get("MONGO_DB_URL"))

class selling_house_routes:
    def __init__(self):
        self.__router = APIRouter()
        self.__selling_house_controller = selling_house_controller(client)
        self.config_routes()
        
    def config_routes(self):
        self.__router.add_api_route("/generate_new_selling_ID", self.__selling_house_controller.generate_new_selling_ID, methods=["GET"])
        self.__router.add_api_route("/{seller_id}", self.__selling_house_controller.get_all_seller_house_listings, methods=["GET"])
        self.__router.add_api_route("/{selling_id}", self.__selling_house_controller.delete_house_listing, methods=["DELETE"])
        self.__router.add_api_route("/", self.__selling_house_controller.save_house_listing, methods=["POST"])
        self.__router.add_api_route("/saveHouseImages/{selling_id}/{seller_id}", self.__selling_house_controller.save_house_images, methods=["PUT"])
        
    def get_router(self):
        return self.__router