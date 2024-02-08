import os
from fastapi import APIRouter
from routes.seller_routes import seller_routes
from routes.selling_house_routes import selling_house_routes
from routes.auth_routes import auth_routes
from motor.motor_asyncio import AsyncIOMotorClient

main_router = APIRouter()
url_prefix = "/api/v1"

# Creating a new endpoint for the main router to handle requests with /sellers/
sellerRoutes = seller_routes()
sellingHousesRoutes = selling_house_routes()
authRoutes = auth_routes()

client = AsyncIOMotorClient(os.environ.get("MONGO_DB_URL"))

# Register routes with FastAPI
# Creating router middlwares to connect all routers into one location
main_router.include_router(sellerRoutes.get_router(), prefix=f"{url_prefix}/seller")
main_router.include_router(sellingHousesRoutes.get_router(), prefix=f"{url_prefix}/selling_house")
main_router.include_router(authRoutes.get_router(), prefix=f"{url_prefix}/auth")