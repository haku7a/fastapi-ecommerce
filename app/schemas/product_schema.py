# app/schemas/product_schema.py
from typing import Optional
from sqlmodel import SQLModel, Field

class ProductBase(SQLModel):
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0)

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int

class ProductUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)