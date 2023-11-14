from typing import Union

from fastapi import Cookie, FastAPI
from typing_extensions import Annotated

app = FastAPI()


# 声明 Cookie 参数

# 声明 Cookie 参数的结构与声明 Query 参数和 Path 参数时相同。
# 第一个值是参数的默认值，同时也可以传递所有验证参数或注释参数，来校验参数：

# Cookie 、Path 、Query是兄弟类，它们都继承自公共的 Param 类

@app.get("/items/")
async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id": ads_id}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)