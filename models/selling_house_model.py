from pydantic import BaseModel

class SellingHouse(BaseModel):
    selling_id: str
    seller_id: str
    name: str
    description: str
    address: str
    price: float
    bedrooms: int
    bathrooms: int
    area: float
    houseAge: int
    landSize: float
    location: dict
    houseImages: list
    ownerName: str
    ownerContact1: str
    ownerContact2: str
    saleDate: str
    saleTime: str