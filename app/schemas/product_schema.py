# app/schemas/product_schema.py
from typing import Optional
from sqlmodel import SQLModel, Field

class ProductBase(SQLModel):
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0)
    sku: Optional[str] = Field(default=None, max_length=50)
    stock_quantity: int = Field(default=0, ge=0)
    is_active: bool = Field(default=True)

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int

class ProductUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
    sku: Optional[str] = Field(default=None, max_length=50)
    stock_quantity: Optional[int] = Field(default=None, ge=0)
    is_active: Optional[bool] = None