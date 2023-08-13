import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "My name is Ou"

@app.get("/data")
def read_item(temp: int = 0):
    print(temp)
    return {"Temp  : ":temp}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)