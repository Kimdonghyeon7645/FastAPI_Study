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
    i_id: int
    # b_id: int
    name: str
    b_type: BuildingType
    bjdong: str
    lat: float
    lon: float
    address: str
    manage_team: str
    area: str
    completion_date: int
    cusno: int
    meter_no: int
    rate_plan: str
    meter_reading_date: int
    contract_e: int
    peak_e: int

class EnergyUsage(BaseModel):
    e_id: int
    b_id: int
    month: int
    usage: float
