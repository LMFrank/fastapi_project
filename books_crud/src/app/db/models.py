# -*- coding: utf-8 -*-
from typing import Tuple
from app.configs import engine, metadata
from sqlalchemy import Table, Column, Integer, String, DateTime, TIMESTAMP
from sqlalchemy.sql import func


def timestamps() -> Tuple[Column, Column]:
    return (
        Column("create_time", TIMESTAMP(timezone=True), server_default=func.now(), nullable=False),
        Column("update_time", TIMESTAMP(timezone=True), server_default=func.now(), nullable=False, onupdate=func.now())

    )

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("book", String(32), nullable=False),
    Column("author", String(32), nullable=False),
    *timestamps()
)


if __name__ == '__main__':
    metadata.create_all(engine)