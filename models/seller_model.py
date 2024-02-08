from pydantic import BaseModel

class Seller(BaseModel):
    seller_id: str
    seller_name: str
    seller_contact_01: str
    seller_contact_02: str
    seller_address: str
    seller_email: str