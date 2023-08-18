from fastapi import FastAPI
from pydantic import BaseModel
from utils import generate_description
app = FastAPI()

class Order(BaseModel):
    product:str
    units:int

class Product(BaseModel):
    name: str
    notes: str


@app.get("/ok")
async def ok_endpoint():
    return {'message':'ok'}

@app.get("/hello")
async def hello_endpoint(name:str = 'World'):
    return {'message':f"Hello {name}!!"}

@app.post("/orders")
async def orders(product:str, units:int):
    return {'message':f'Order for {units} units of {product} is placed successfully'}

@app.post("/orders_pydantic")
async def orders(order:Order):
    return {'message':f'Order for {order.units} units of {order.product} is placed successfully'}

@app.post("/product_description")
async def generate_product_description(product: Product):
    description = generate_description(f"Product name: {product.name}, Notes: {product.notes}")
    return {"product_description":description}