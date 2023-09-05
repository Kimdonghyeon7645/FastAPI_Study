from pydantic import BaseModel
from enum import Enum

class BuildingType(str, Enum):
    주민복지시설 = "주민복지시설"
    노인복지시설 = "노인복지시설"
    체육시설 = "체육시설"
    업무시설 = "업무시설"
    

class Building(BaseModel):
    b_id: int
    name: str
    b_type: BuildingType
    bjdong: str
    lat: float
    lon: float

class BuildingInfo(BaseModel):
    b_id: int
    address: str
    manage_team: str
    area: float
    completion_date: str
    building_image: str
    cusno: int
    meter_no: int
    rate_plan: str
    meter_reading_date: int

class PowerUsage(BaseModel):
    b_id: int
    datetime: str
    usage: float
