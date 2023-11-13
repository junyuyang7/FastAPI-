from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    print(item.dict())
    return item, 'hhhhh'

@app.put("/items/{item_id}")
async def create_item1(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

@app.put("/items2/{item_id}")
async def create_item2(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)