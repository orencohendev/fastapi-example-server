from fastapi.routing import APIRouter

health_router = APIRouter()


@health_router.get("/healthz")
def healthz():
    return {"status": "ok"}
