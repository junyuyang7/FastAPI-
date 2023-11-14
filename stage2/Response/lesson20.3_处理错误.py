from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

# 覆盖默认异常处理器
# FastAPI 自带了一些默认异常处理器。

# 触发 HTTPException 或请求无效数据时，这些处理器返回默认的 JSON 响应结果。

# 不过，也可以使用自定义处理器覆盖默认异常处理器。

@app.exception_handler(StarletteHTTPException) # 重写HTTPException错误处理程序
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError) # 导入超越请求验证异常
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)