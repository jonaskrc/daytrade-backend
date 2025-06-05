
from fastapi import FastAPI
from routers import auth, signals
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]  # Para produção, usar domínios específicos

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(signals.router, prefix="/signals")

@app.get("/")
def root():
    return {"message": "API Online"}
