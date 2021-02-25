name = input('What is your name? ')
days = input('How many days did you work thin month? ')
workedHours = input('How many hours did you work in a day?')
salary = input('What is your salary per hour? ')
workeddays = int(workedHours) * int(days)
week = int(workedHours) * 5
weektotal = int(week) * int(salary)
totalsalary = int(workeddays) * int(salary)
total = totalsalary * 24 / 100
totalweek = weektotal * 24 / 100
print(
    'Hey ', name ,'!',
    '\nYour salary for a week is: ', weektotal, 'With 24% taxes is: ', totalweek,
    '\nYour salary for a month is: ', totalsalary, 'With 24% taxes is: ', total
    )


