from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl

class CustomerInfo(BaseModel):
    id: int
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class LineItem(BaseModel):
    id: int
    product_id: int
    product_title: str
    quantity: int
    price: float

class Order(BaseModel):
    id: int
    order_number: str
    created_at: str  # Use datetime if you prefer to work with datetime objects
    total_price: float
    subtotal_price: Optional[float] = None
    total_tax: Optional[float] = None
    currency: str
    customer: Optional[CustomerInfo] = None
    line_items: List[LineItem] = []
    order_status_url: Optional[HttpUrl] = None

class OrdersResponse(BaseModel):
    orders: List[Order]
