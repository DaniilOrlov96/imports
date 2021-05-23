from datetime import datetime
from Application.salary import calculate_salary
from db.people import get_employees

if __name__ == '__main__':
    calculate_salary()
    date = datetime.today()
    print('now', date)

get_employees()
date = datetime.today()
print('now', date)

