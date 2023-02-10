from datetime import datetime

class Employee():

    def __init__(self, name: str = "No definido", dni: str = "000", birthday: str = "??/??/???", join_date: str = "??/??/???", salary: float = 0):
        self.name: str = name
        self.dni: str = dni
        self.birthday: str = birthday
        self.join_date: str = join_date
        self.salary: float = salary

    def Antiquity(self) -> float:
        join_date_diff = datetime.date(datetime.now()) - self.join_date
        return((join_date_diff.day + join_date_diff.seconds)/86400) / 365
