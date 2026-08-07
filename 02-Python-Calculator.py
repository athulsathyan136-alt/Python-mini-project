print('*********Calculator**********')
num1=int(input("Enter the First Number:"))
num2 =int(input('Enter the Second Number:'))

print('\nChoose an Operator:')
print('1.Addition:')
print('2.subtraction:')
print('3.Multiplication:')
print('4.Division:')

print()

choice = input('Enter Your Choice:')

if choice == '1':
    print('Result:',num1+num2)
elif choice == '2':
    print('Result:',num1-num2)
elif choice == '3':
    print('Result:',num1*num2)
elif choice == '4':
    print('Result:',num1/num2)
else:
    print('Invalid Choice')        

        

