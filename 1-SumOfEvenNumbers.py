#!C:\Users\kajjarapu\AppData\Local\Programs\Python\Python36-32\python.exe
import sys

def Sum(n1,n2):
    result1 = 0
    result2 = 0
    if n2>n1:
        for n in range(n1,n2+1):
           if n%6==0:
               result1+=n
           if n%2==0:
               result2+=n
               
        print("Sum of multiple of 6 is {0}".format(result1))
        print("Sum of even numbers is {0}".format(result2))
    else:
        print("Invalid range")
      
    
if __name__ == '__main__':
    n1,n2 = eval(input("Enter lower and upper bound numbers of a range: "))
    Sum(n1,n2)
  
