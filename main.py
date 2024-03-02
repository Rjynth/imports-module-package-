import application.salary
import application.db.people
from datetime import datetime

if __name__ == '__main__':
    print("Дата:", datetime.now())

    employees = application.db.people.get_employees()
    print("Работники:", employees)

    salary = application.salary.calculate_salary()
    print("Общая зарплата:", salary, 'денег')