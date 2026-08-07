name =input('Enter Student Name:')
roll=int(input('Enter Roll Number:'))
age=int(input('Enter Age:'))
cou = input('Enter Course:')

python=int(input('Enter Python Marks:'))
sql=int(input('Enter SQL Marks:'))
ai=int(input('Enter AI Marks:'))

total= python+sql+ai
avg=(python+sql+ai)/3

print('\n===== Student Report======\n')

print('Name:',name)
print('Roll Number:',roll)
print('Age:',age)
print('Course:',cou)


print('Python Marks:',python)
print('SQL Marks:',sql)
print('AI Marks:',ai)



print('Total Marks:',total)
print('Average:',avg)