from typing import NewType

from pydantic.main import BaseModel
from pydantic.types import ConstrainedDecimal

IMO = NewType("IMO", int)


class Latitude(ConstrainedDecimal):
    ge = -90
    le = 90


class Longitude(ConstrainedDecimal):
    ge = -180
    le = 180


class Coordinates(BaseModel):
    latitude: Latitude
    longitude: Longitude


class VesselLocation(BaseModel):
    imo: IMO
    latitude: Latitude
    longitude: Longitude
