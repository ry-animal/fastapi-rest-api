# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from mangum import Mangum

# app = FastAPI()
# handler = Mangum(app)

# class Item(BaseModel):
#     text: str
#     is_done: bool = False

# items = []

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

# @app.post("/items")
# def create_item(item: Item):
#     items.append(item)
#     return items

# @app.get("/items", response_model=list[Item])
# def list_items(limit: int = 10):
#     return items[0:limit]

# @app.get("/items/{item_id}", response_model=Item)
# def get_item(item_id: int) -> Item:
#     if item_id < len(items):
#         return items[item_id]
#     else:
#         raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

## Simplify for now
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
