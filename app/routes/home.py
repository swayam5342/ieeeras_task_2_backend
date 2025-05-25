from fastapi import APIRouter,HTTPException
from app.schemas.book import Book
from app.services.db import db


root = APIRouter()
collection = db["books"]



@root.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}


@root.get("/items", response_model=list[Book])
def read_items(
    skip: int = 0,
    limit: int = 10,
    author: str | None = None,
    genre: str | None = None,
    year: int | None = None,
):
    query = {}
    if author:
        query["author"] = author
    if genre:
        query["genre"] = genre
    if year:
        query["year"] = year
    items = list(collection.find(query).skip(skip).limit(limit))
    if not items:
        raise HTTPException(status_code=404, detail="No items found")
    return [Book(**{k: v for k, v in item.items() if k != "_id"}) for item in items]

@root.post("/items", response_model=Book)
def create_item(item: Book):
    existing = collection.find_one({"id": item.id})
    if existing:
        raise HTTPException(status_code=400, detail="Item already exists")
    collection.insert_one(item.model_dump())
    return item


@root.put("/items/{item_id}", response_model=Book)
def update_item(item_id: int, item: Book):
    if item.id != item_id:
        raise HTTPException(status_code=400, detail="Item ID mismatch")
    result = collection.update_one({"id": item_id}, {"$set": item.model_dump()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@root.delete("/items/{item_id}")
def delete_item(item_id: int):
    result = collection.delete_one({"id": item_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
