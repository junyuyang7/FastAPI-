from fastapi import FastAPI, HTTPException, Header
from typing_extensions import Annotated
from typing import Union

app = FastAPI()

items = {'foo': 'The Foo Wrestlers'}

@app.get('/items/{item_id}')
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail='Item not found')
    return {'item': items[item_id]}

@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str, 
        user_agent: Annotated[Union[str, None], Header()] = None):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id], 'user_agent': user_agent}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)