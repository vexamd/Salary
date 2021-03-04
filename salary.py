class CalculatorNotNumberException(Exception):
    print('Hey this is not a number')
class salarycalculate:
    name = input('What is your name? ')
    days = input('How many days did you work thin month? ')
    workedHours = input('How many hours did you work in a day?')
    contract = input('What is your salary on contract? ')
    salary = input('What is your salary per hour? ')
    workeddays = int(workedHours) * int(days)
    ç
    workedsalary = workeddays * salary
    if not isinstance(workeddays, int) or not isinstance(salary, int):
        raise CalculatorNotNumberException()
    totalgross = workedsalary + contract
    if not isinstance(salary, int):
        raise CalculatorNotNumberException()
    netsalary = totalgross * 24 / 100
    totalnet = totalgross - netsalary
    print(
        'Hey ', name ,'!',
        '\nGross salary: ', totalgross, 'Lei'
        '\nNet salary: ',  totalnet, 'Lei'
        '\nContract salary: ', contract, 'Lei'
        '\nWorked salary: ', workedsalary, 'Lei'
        )
