from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# The class `HolidayBase` defines properties for a holiday including location, start and end dates,
# city, and country.

class HolidayBase(BaseModel):
    location: str
    start_date: datetime
    end_date: datetime
    city: str
    country: str


# The above code defines three classes for creating, updating, and retrieving holiday information with
# additional attributes for location, start and end dates, city, country, and creation timestamp.
class HolidayCreate(HolidayBase):
    location: str
    start_date: datetime
    end_date: datetime
    city: str
    country: str

class HolidayUpdate(HolidayBase):
    pass


class Holiday(HolidayBase):
    id: int
    created_when: Optional[datetime]

    class Config:
        orm_mode = True
