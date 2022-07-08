# -*- coding: utf-8 -*-
from fastapi import APIRouter
from app.api.api_1_0 import ping, books

router = APIRouter()
router.include_router(ping.router)
router.include_router(books.router)
