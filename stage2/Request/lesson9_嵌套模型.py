from typing import List, Set, Dict, Union

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

# 你可以将一个属性定义为拥有子元素的类型。例如 Python list：
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    image: Union[List[Image], None] = None
# 这将使 tags 成为一个由元素组成的列表。不过它没有声明每个元素的类型。tags: list = []
# 声明具有子类型的 List (my_list: List[str])

class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: List[Item]

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)


# 总结

# 使用 FastAPI 你可以拥有 Pydantic 模型提供的极高灵活性，同时保持代码的简单、简短和优雅。

# 而且还具有下列好处：
    # 编辑器支持（处处皆可自动补全！）
    # 数据转换（也被称为解析/序列化）
    # 数据校验
    # 模式文档
    # 自动生成的文档