from constants.energy_usage_dat import ENERGY_USAGE
from constants.public_building_dat import PUBLIC_BUILDINGS
from constants.public_building_info_dat import PUBLIC_BUILDINGS_INFOS
from models import Building, BuildingInfo, EnergyUsage


_buildings = [Building(b_id=i, **row) for i, row in enumerate(PUBLIC_BUILDINGS)]
_usages = [EnergyUsage(e_id=i, **row) for i, row in enumerate(ENERGY_USAGE)]
_building_infos = [BuildingInfo(i_id=i, **row) for i, row in enumerate(PUBLIC_BUILDINGS_INFOS)]


def get_buildings():
    return _buildings


def get_buildings_usages(bjdong = None, month = None):
    return [{**b.dict(), "usages": [{u.month: u.usage} for u in _usages if u.b_id == b.b_id]}  for b in _buildings if not bjdong or b.bjdong == bjdong]


def get_usages():
    return _usages
 
def get_building_infos():
    return _building_infos