from typing import Any
from fastapi.responses import StreamingResponse
from io import BytesIO
from zipfile import ZipFile
import json

class ZipHelper:

    @staticmethod
    def get_zip(data: Any) -> StreamingResponse:
        data_bytes = json.dumps(data).encode("utf-8")
        zip_buffer = BytesIO()
        with ZipFile(zip_buffer, "w") as zip_file:
            zip_file.writestr(f"report.json", data_bytes)
        headers = {
            "Content-Disposition": f"attachment; filename=\"report.zip\""
        }
        return StreamingResponse(iter([zip_buffer.getvalue()]), headers=headers)