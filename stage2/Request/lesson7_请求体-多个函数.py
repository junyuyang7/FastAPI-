# 混合使用 Path、Query 和请求体参数

from typing import Union

from fastapi import FastAPI, Path, Query, Body
# Body 同样具有与 Query、Path 以及其他后面将看到的类完全相同的额外校验和元数据参数。
from pydantic import BaseModel
from typing_extensions import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    importance: Annotated[int, Body()],
    item: Annotated[Item, Body(embed=True)],
    q: Union[str, None] = Query(default=None, regex='^aaa'),
    user: Union[User, None] = None,
):
    results = {"item_id": item_id, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)

# 总结

# 你可以添加多个请求体参数到路径操作函数中，即使一个请求只能有一个请求体。
# 但是 FastAPI 会处理它，在函数中为你提供正确的数据，并在路径操作中校验并记录正确的模式。
# 你还可以声明将作为请求体的一部分所接收的单一值。
# 你还可以指示 FastAPI 在仅声明了一个请求体参数的情况下，将原本的请求体嵌入到一个键中。
