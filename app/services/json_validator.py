# app/services/json_validator.py
from pydantic import BaseModel
from typing import List, Union, Dict, Optional

class Section(BaseModel):
    title: str
    type: str
    content: Union[str, Dict] = ""   # existing content
    data: Optional[Dict] = None      # NEW: optional structured data for AI

class ReportInput(BaseModel):
    title: str
    date: str
    author: str
    sections: List[Section]
