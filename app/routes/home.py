from fastapi import APIRouter,HTTPException
from app.schemas.book import Book

root = APIRouter()

db={
    1:{
        "id":1,
        "title":"DSA in Java",
        "author":"John Doe",
        "year":2019,
        "genre":"Programming",
    }
}


@root.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}

@root.get("/items",response_model=list[Book])
def read_items():
    if db:
        return list(db.values())
    else:
        raise HTTPException(status_code=404, detail="No items found")

@root.post("/items", response_model=Book)
def create_item(item: Book):
    if item.id in db:
        raise HTTPException(status_code=400, detail="Item already exists")
    db[item.id] = item.model_dump()
    return item

@root.put("/items/{item_id}", response_model=Book)
def update_item(item_id: int, item: Book):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.id != item_id:
        raise HTTPException(status_code=400, detail="Item ID mismatch")
    db[item_id] = item.model_dump()
    return item

@root.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return {"message": "Item deleted successfully"}