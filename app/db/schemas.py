# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    book: str = Field(..., min_length=3, max_length=32)
    author: str = Field(..., min_length=3, max_length=32)


class BookDB(BookSchema):
    id: int