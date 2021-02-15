from typing import Optional, Any

from pydantic import BaseModel


# Shared properties
class GridBase(BaseModel):
    gridID: Any
    latMin: float
    lngMin: float
    latMax: float
    lngMax: float
    P_NAME_E: str
    A_NAME_E: str
    T_NAME_E: str
    P_CODE: int
    A_CODE: int
    T_CODE: int


class GridDB(GridBase):
    class Config:
        orm_mode = True


# Properties to receive on grid creation
class GridCreate(GridBase):
    pass

class GridUpdate(GridBase):
    pass

