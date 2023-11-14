from typing import Any, Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None

# 永远不要存储用户的明文密码，也不要在响应中发送密码。

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)

# FastAPI 将会负责过滤掉未在输出模型中声明的所有数据（使用 Pydantic）