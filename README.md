# Hacktober1
Hacktober Fest
program fizzbuzz
  Do i = 1 to 100 
    set print_number to true
    If i is divisible by 3
      print "Fizz"
      set print_number to false
    If i is divisible by 5
      print "Buzz" 
      set print_number to false
    If print_number, print i
    print a newline
  end do
