# -*- coding: utf-8 -*-
from fastapi import APIRouter, Path, HTTPException
from app.db.schemas import BookDB, BookSchema
from app.api.api_1_0 import crud
from typing import List


router = APIRouter()


@router.post("/book", response_model=BookDB, status_code=201)
async def create_book(payload: BookSchema):
    book_id = await crud.post(payload)

    response_object = {
        "id": book_id,
        "book": payload.book,
        "author": payload.author,
    }
    return response_object

@router.get("/book/{id}", response_model=BookDB)
async def get_book(id: int = Path(..., gt=0)):
        book = await crud.get(id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

@router.get("/book", response_model=List[BookDB])
async def get_all_books():
    return await crud.get_all()

@router.put("/book/{id}", response_model=BookDB)
async def update_book(payload: BookSchema, id: int = Path(..., gt=0)):
    book = await crud.get(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book_id = await crud.put(id, payload)

    response_object = {
        "id": book_id,
        "book": payload.book,
        "author": payload.author,
    }
    return response_object

@router.delete("/book/{id}", response_model=BookDB)
async def delete_book(id: int = Path(..., gt=0)):
    book = await crud.get(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    await crud.delete(id)
    return book