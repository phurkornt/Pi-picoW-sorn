"""
 This Code is on computer only
 # FastAPI
"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/item")
def read_item(sw: int = 0):
    print(sw)
    return {"switch status : ":sw}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)