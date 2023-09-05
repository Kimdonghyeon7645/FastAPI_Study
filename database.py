
from constants.public_building_dat import PUBLIC_BUILDINGS
from models import Building


_data = [Building(b_id=i, **row) for i, row in enumerate(PUBLIC_BUILDINGS)]

def add_item(item):
    _data.append(item)
    return item

def get_items():
    return _data
