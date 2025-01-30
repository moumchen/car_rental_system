from datetime import datetime

class Car:
    """
        This Class is the entity class of table car
    """
    def __init__(self,
                 id = None,
                 make: str = "",
                 model: str = "",
                 manufactured_year: str = "",
                 mileage: int = 0,
                 available: int = 1,
                 min_lease_limit: int = 0,
                 max_lease_limit: int = 0,
                 deleted_flag: int = 0,
                 created_time: datetime = datetime.now(),
                 updated_time: datetime = datetime.now(),
                 deleted_time: datetime = datetime(1900, 1, 1),
                 daily_rent: float = 0.00,
                 extra_fee: float = 0.00):
        self.id = id
        self.make = make
        self.model = model
        self.manufactured_year = manufactured_year
        self.mileage = mileage
        self.available = available
        self.min_lease_limit = min_lease_limit
        self.max_lease_limit = max_lease_limit
        self.deleted_flag = deleted_flag
        self.created_time = created_time
        self.updated_time = updated_time
        self.deleted_time = deleted_time
        self.daily_rent = daily_rent
        self.extra_fee = extra_fee

    def __repr__(self):
        return (f"Car(id={self.id}, make='{self.make}', model='{self.model}', "
                f"manufactured_year='{self.manufactured_year}', mileage={self.mileage}, "
                f"available={self.available}, min_lease_limit={self.min_lease_limit}, "
                f"max_lease_limit={self.max_lease_limit}, deleted_flag={self.deleted_flag}, "
                f"created_time={self.created_time}, updated_time={self.updated_time}, "
                f"deleted_time={self.deleted_time}, daily_rent={self.daily_rent}, "
                f"extra_fee={self.extra_fee})")
