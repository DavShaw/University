from datetime import datetime, date

class Employee():

    def __init__(self, name: str, dni: str, birthday: date, join_date: date, salary: float):
        self.name: str = name
        self.dni: str = dni
        self.birthday: date = birthday
        self.join_date: date = join_date
        self.salary: float = salary



    def Antiquity(self) -> float:
        join_date_diff = datetime.date(datetime.now()) - self.join_date
        return round(((join_date_diff.days + join_date_diff.seconds / 86400) / 365), 1)
