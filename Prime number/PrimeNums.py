# Author:    Mahdi Safarian
# Date:      04/20/20
# Subject:   Finde Prime Numbers.
while True:
   num = int(input("Please enter the number:"))
   if num > 1:


      for i in range(2, num):


         if (num % i) == 0:
            print(num, "is not a prime number")
            break
      else:
         print(num, "is a prime number")
   else:
      print(num, "is not a prime number")
