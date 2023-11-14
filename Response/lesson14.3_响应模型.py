from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 你的响应模型可以具有默认值，例如：
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

# 举个例子，当你在 NoSQL 数据库中保存了具有许多可选属性的模型，但你又不想发送充满默认值的很长的 JSON 响应。

# 使用 response_model_exclude_unset 参数
# 你可以设置路径操作装饰器的 response_model_exclude_unset=True 参数

@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]

# response_model_include 和 response_model_exclude

    # 你还可以使用路径操作装饰器的 response_model_include 和 response_model_exclude 参数。
    # 它们接收一个由属性名称 str 组成的 set 来包含（忽略其他的）或者排除（包含其他的）这些属性。

@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={'tax'})
async def read_item_public(item_id: str):
    return items[item_id]

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)