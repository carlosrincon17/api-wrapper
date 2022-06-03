from constants.file_types import FileTypes
from fastapi import FastAPI, Request, status, Response

from helpers.rest_client import RestClient
from helpers.zip_helper import ZipHelper
from settings import Settings


app = FastAPI()
settings = Settings()

@app.get("/{resource}")
async def filter(request: Request,  response: Response, resource: str, format: str = FileTypes.JSON):
    client = RestClient(
        settings.api_url
    )
    _response = client.get(query_params=request.query_params, resource=resource)
    response.status_code = _response.status_code
    if format == FileTypes.ZIP and _response.status_code == status.HTTP_200_OK:
        return ZipHelper.get_zip(
            data=_response.data
        )
    return _response