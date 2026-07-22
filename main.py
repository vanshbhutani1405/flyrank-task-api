from fastapi import FastAPI, HTTPException, status
from fastapi.responses import Response
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Task API",
    description="Simple CRUD API using FastAPI",
    version="1.0"
)

