from typing import Any
from pydantic import BaseModel

class Response(BaseModel):
    status_code: int = 0
    data: Any