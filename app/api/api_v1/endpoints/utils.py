from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# from app import crud, models, schemas
# from app.api import deps

router = APIRouter()


@router.get("/")
def index():
    return {"Hello": "Worlds"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}