# Employee Salary Slip
# Built with basic Python and simple maths formulas.
# Takes a name, basic salary, bonus and tax percentage,
# then prints the gross salary, tax amount and net salary.

employee_name = input('ENTER NAME HERE : ')
basic_salary = float(input('ENTER YOUR BASIC SALARY : '))
bonus_amount = float(input('ENTER YOUR BONUS AMOUNT HERE : '))
tax_percentage = float(input('ENTER YOUR TAX PERCENTAGE : '))

gross_salary = basic_salary + bonus_amount
tax_amount = (gross_salary * tax_percentage) / 100
net_salary = gross_salary - tax_amount

print('')
print('---------------------------------------------------------')
print('')
print('welcome ', employee_name, '!')
print('')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(' ')

print('According to your basic salary (', basic_salary, ') :')
print('your gross salary is :', gross_salary)
print('your tax amount is :', tax_amount)
print('your net salary is :', net_salary)
