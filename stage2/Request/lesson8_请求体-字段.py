# 与使用 Query、Path 和 Body 在路径操作函数中声明额外的校验和元数据的方式相同，
# 你可以使用 Pydantic 的 Field 在 Pydantic 模型内部声明校验和元数据。
from typing import Union

from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel, Field
from typing_extensions import Annotated

app = FastAPI()

# Field 的工作方式和 Query、Path 和 Body 相同，包括它们的参数等等也完全相同。
class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)

# 总结

# 你可以使用 Pydantic 的 Field 为模型属性声明额外的校验和元数据。
# 你还可以使用额外的关键字参数来传递额外的 JSON Schema 元数据。