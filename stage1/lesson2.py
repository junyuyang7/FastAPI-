from starlette.requests import Request
from fastapi import FastAPI
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="template")

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'hello':'Hi...'})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)