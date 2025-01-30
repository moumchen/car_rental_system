from datetime import datetime

class LeaseDetail:
    """
          This Class is the entity class of table lease_detail
    """

    def __init__(self,
                 id = None,
                 user_id: int = 0,
                 car_id: int = 0,
                 lease_start_time: datetime = datetime(1900, 1, 1),
                 lease_end_time: datetime = datetime(1900, 1, 1),
                 interval_days: int = 0,
                 rent: float = 0.00,
                 deleted_flag: int = 0,
                 created_time: datetime = datetime.now(),
                 updated_time: datetime = datetime.now(),
                 deleted_time: datetime = datetime(1900, 1, 1),
                 approved_flag: int = 0,
                 refusal_reason: str = ""):
        self.id = id
        self.user_id = user_id
        self.car_id = car_id
        self.lease_start_time = lease_start_time
        self.lease_end_time = lease_end_time
        self.interval_days = interval_days
        self.rent = rent
        self.deleted_flag = deleted_flag
        self.created_time = created_time
        self.updated_time = updated_time
        self.deleted_time = deleted_time
        self.approved_flag = approved_flag
        self.refusal_reason = refusal_reason

    def __repr__(self):
        return (f"LeaseDetail(id={self.id}, user_id={self.user_id}, car_id={self.car_id}, "
                f"lease_start_time={self.lease_start_time}, lease_end_time={self.lease_end_time}, "
                f"interval_days={self.interval_days}, rent={self.rent}, deleted_flag={self.deleted_flag}, "
                f"created_time={self.created_time}, updated_time={self.updated_time}, "
                f"deleted_time={self.deleted_time}, approved_flag={self.approved_flag}, "
                f"refusal_reason={self.refusal_reason})")
