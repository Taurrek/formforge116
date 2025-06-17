from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .auth_api import router as auth_router
from .oauth_api import router as oauth_router
from .push_api import router as push_router
from .admin_api import router as admin_router
from .user_api import router as user_router
from .forms_api import router as forms_router
from .performance_api import router as perf_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(oauth_router)
app.include_router(push_router)
app.include_router(admin_router)
app.include_router(user_router)
app.include_router(forms_router)
app.include_router(perf_router)

@app.get("/api/health")
async def health():
    return {"status": "ok"}
