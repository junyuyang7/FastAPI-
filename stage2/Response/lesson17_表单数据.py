from fastapi import FastAPI, Form

app = FastAPI()

# 例如，OAuth2 规范的 "密码流" 模式规定要通过表单字段发送 username 和 password。
# 该规范要求字段必须命名为 username 和 password，并通过表单字段发送，不能用 JSON
# 使用 Form 可以声明与 Body （及 Query、Path、Cookie）相同的元数据和验证。
@app.post("/login/")
async def login(username: str = Form(default='rrrr'), password: str = Form(default='rrrr')):
    return {"username": username}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)