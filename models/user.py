from datetime import datetime

class User:
    """
         This Class is the entity class of table user
    """

    def __init__(self,
                 id=None,
                 username: str = "",
                 password: str = "",
                 role_type: int = 0,
                 deleted_flag: int = 0,
                 created_time: datetime = datetime.now(),
                 deleted_time: datetime = datetime(1900, 1, 1),
                 updated_time: datetime = datetime.now()):
        self.id = id
        self.username = username
        self.password = password
        self.role_type = role_type
        self.deleted_flag = deleted_flag
        self.created_time = created_time
        self.deleted_time = deleted_time
        self.updated_time = updated_time


    def __repr__(self):
        return (f"User(id={self.id}, username='{self.username}', password='{self.password}', "
                f"role_type={self.role_type}, deleted_flag={self.deleted_flag}, "
                f"created_time={self.created_time}, deleted_time={self.deleted_time}, "
                f"updated_time={self.updated_time})")
