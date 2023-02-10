from datetime import datetime

class Employee():

    def __init__(self, name: str = "No definido", dni: str = "000", birthday: str = "??/??/???", join_date: str = "??/??/???", salary: float = 0):
        self.name: str = name
        self.dni: str = dni
        self.birthday: str = birthday
        self.join_date: str = join_date
        self.salary: float = salary

    def Antiquity(self):
        join_date_diff = datetime.date(datetime.now()) - self.join_date
        return((join_date_diff.day + join_date_diff.seconds)/86400) / 365




David = Employee("David", "29/08/2009", "02/01/2018",35000)
Alfonso = Employee("Alfonso", "01/12/2001", "21/11/2015",31000)
Martin = Employee("Martin", "25/05/2003", "05/02/2021",45000)