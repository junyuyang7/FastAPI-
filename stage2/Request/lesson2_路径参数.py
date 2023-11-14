from fastapi import FastAPI
from enum import Enum

class Name(str, Enum):
    Allen = 'aa'
    Jon = 'bb'
    Bob = 'cc'

app = FastAPI()

@app.get("/{who}")
async def get_day(who: Name):
    if who == Name.Allen:
        return {"who": who, "message": "aa is aa"}
    if who.value == 'bb':
        return {"who": who, "message": "bb is bb"}
    return {"who": who, "message": "cc is cc"}

@app.get("/")
async def main():
    return {"message": "Hello FastAPI"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
