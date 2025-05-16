from typing import Optional
from sqlmodel import Field, SQLModel

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: Optional[str] = None
    price: float = Field(gt=0)
    sku: Optional[str] = Field(default=None, unique=True, index=True, max_length=50)
    stock_quantity: int = Field(default=0, ge=0)
    is_active: bool = Field(default=True)