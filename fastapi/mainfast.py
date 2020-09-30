# -*- coding: utf-8 -*-


from typing import Optional

from fastapi import FastAPI,Query
from pydantic import BaseModel
#uvicorn main:app --reload
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

class reqbody(BaseModel):
    productId: str
    isPay: int
    name: str
    mobile: str
    size: int
    price: Optional[str] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": Item.name, "item_id": item_id}

@app.post("/items/qumaip/create")
def read_item(reqbody:reqbody):
    return {"success": 1, "message": "成功","data":{
        "id": "23",
        "userId": "3",
        "distributorId": "1",
        "supplierId": "9",
        "prodTitle": "长隆水上乐园",
        "name": "李好",
        "mobile": "13472418383",
        "orderTime": 1363937085,
        "sendStatus": 1,
        "productId": "11",
        "price": "116.00",
        "sumPrice": "232.00",
        "size": "2",
        "remainNums": "1",
        "usedNums": "0",
        "appBackNums": "0",
        "valStartRQ": "2016-05-0317: 22: 36",
        "valEndRQ": "2017-04-2523: 59: 59",
        "qrcode": "AQYRctFfiZDMwOGRKRlZmRml0QnRSRkI=",
        "code": "909912,909913"
},"serialno": 20160426154500080}

@app.post("/items/qumaip/createfalse")
def read_item(reqbody:reqbody):
    return {"success": "false", "message": "成功","data":{
        "id": "23",
        "userId": "3",
        "distributorId": "1",
        "supplierId": "9",
        "prodTitle": "长隆水上乐园",
        "name": "李好",
        "mobile": "13472418383",
        "orderTime": 1363937085,
        "sendStatus": 1,
        "productId": "11",
        "price": "116.00",
        "sumPrice": "232.00",
        "size": "2",
        "remainNums": "1",
        "usedNums": "0",
        "appBackNums": "0",
        "valStartRQ": "2016-05-0317: 22: 36",
        "valEndRQ": "2017-04-2523: 59: 59",
        "qrcode": "AQYRctFfiZDMwOGRKRlZmRml0QnRSRkI=",
        "code": "909912,909913"
},"serialno": 20160426154500080}




