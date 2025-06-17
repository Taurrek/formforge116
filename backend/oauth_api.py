from fastapi import APIRouter, Request, HTTPException
from starlette.config import Config
from starlette.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth

config = Config(".env")
oauth = OAuth(config)
oauth.register(
    name="google",
    client_id=config("GOOGLE_CLIENT_ID"),
    client_secret=config("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

router = APIRouter(prefix="/api/auth")

@router.get("/login")
async def login(request: Request):
    redirect_uri = config("GOOGLE_REDIRECT_URI")
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/callback")
async def callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    if not token:
        raise HTTPException(status_code=400, detail="OAuth token missing")
    user = await oauth.google.parse_id_token(request, token)
    # TODO: lookup/create user in your DB, issue JWT
    return {"email": user["email"], "name": user["name"]}
