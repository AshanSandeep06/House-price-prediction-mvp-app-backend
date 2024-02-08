from models.signup_model import SignUp
from models.login_model import Login
from models.seller_model import Seller
from models.user_credentials_model import UserCredentials
import asyncio
from fastapi.responses import JSONResponse

class auth_controller:
    def __init__(self, client):
        self.client = client
        self.db = client['House-Selling-Price-Prediction-DB']
        self.collection_01 = self.db['user_credentials']
        self.collection_02 = self.db['sellers']

    async def auth_signup(self, signup_bean: SignUp):
        # Check if username already exists
        existing_user = await self.collection_01.find_one({'username': signup_bean.username})
        if existing_user:
            response = {"code": "01", "message": f"This {signup_bean.username} - User is Already Exist, Therefore can't be Added", "content": None}
            return JSONResponse(status_code=500, content=response, media_type="application/json")
        else:
            new_seller_obj = Seller(
                seller_id=signup_bean.seller_id,
                seller_name=signup_bean.seller_name,
                seller_contact_01=signup_bean.seller_contact_01,
                seller_contact_02=signup_bean.seller_contact_02,
                seller_address=signup_bean.seller_address,
                seller_email=signup_bean.seller_email
            )
            
            new_user_credentials_obj = UserCredentials(
                username=signup_bean.username,
                password=signup_bean.password,
                seller_id=signup_bean.seller_id
            )
            new_seller = await self.collection_02.insert_one(new_seller_obj.dict())
            if new_seller:
                await self.collection_01.insert_one(new_user_credentials_obj.dict())
            
            response = {"code": "00", "message": "User has been Successfully Registered..!", "content": None}
            return JSONResponse(status_code=200, content=response, media_type="application/json")
    
    async def auth_login(self, login_bean: Login):
        # Find the user by username and password
        user = await self.collection_01.find_one({'username': login_bean.username, 'password': login_bean.password})
        if user:
            response = {"code": "00", "message": "Login Success", "content": user['seller_id']}
            return JSONResponse(status_code=200, content=response, media_type="application/json")
        else:
            response = {"code": "01", "message": "Invalid Credentials", "content": None}
            return JSONResponse(status_code=500, content=response, media_type="application/json")