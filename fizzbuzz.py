#Hacktober Fest program fizzbuzz Do i = 1 to 100 set print_number to true If i is divisible by 3 print "Fizz
# " set print_number to false If i is divisible by 5 print "Buzz" set print_number to false If print_number, 
# print i print a newline end do

print_number = True

for i in range(1, 101):
    if(i%3 == 0):
        print_number = False
        print('Fizz')
        print(i)
    elif( i%5 ==0):
        print_number = False
        print('Buzz')
        print(i)
