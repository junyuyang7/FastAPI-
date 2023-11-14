from typing import Union, List

from fastapi import FastAPI, Header
from typing_extensions import Annotated

app = FastAPI()

# Header 是 Path, Query 和 Cookie 的兄弟类型。它也继承自通用的 Param 类.
# 为了声明headers， 你需要使用Header, 因为否则参数将被解释为查询参数。

@app.get("/items/")
async def read_items(user_agent: Annotated[Union[str, None], Header()] = None,
                     users_agent: Annotated[Union[str, None], Header()] = None):
    return {"User-Agent": user_agent, 'AAA': users_agent}

@app.get('/items2/')
async def read_item2(x_token: List[str] = Header(default=None)):
    return {'X-Token values': x_token}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)