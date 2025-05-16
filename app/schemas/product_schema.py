# app/schemas/product_schema.py
from typing import Optional
from sqlmodel import SQLModel, Field

class ProductBase(SQLModel):
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0)

class ProductCreate(ProductBase):
    pass