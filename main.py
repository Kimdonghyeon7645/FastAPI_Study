from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_building_infos, get_buildings, get_buildings_usages

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 환경에서는 특정 도메인을 지정하세요.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return "^^b"

@app.get("/building/usage")
async def read_building_usage(bjdong: str = ""):
    return get_buildings_usages(bjdong)

@app.get("/building/info")
async def read_building_info():
    return get_building_infos()
