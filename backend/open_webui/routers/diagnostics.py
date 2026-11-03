from typing import Optional
from pydantic import BaseModel, HttpUrl
from fastapi import APIRouter, Depends, HTTPException, status

from open_webui.utils.auth import get_admin_user
from open_webui.utils.diagnostics import probe_url, is_valid_url
from open_webui.constants import ERROR_MESSAGES


router = APIRouter()


class ConnectionProbeRequest(BaseModel):
    url: str
    timeout: Optional[float] = 5.0


@router.post("/connection")
async def probe_connection(form_data: ConnectionProbeRequest, user=Depends(get_admin_user)):
    if not is_valid_url(form_data.url):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid URL")
    result = probe_url(form_data.url, timeout=form_data.timeout or 5.0)
    return result


@router.get("/health")
async def health():
    return {"status": "ok", "service": "TornadoUI"}
