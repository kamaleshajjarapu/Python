def gcd(n1,n2):
   a=n1
   b=n2
   while a!=b:
    if b>a:
       b=b-a
    else:
       a=a-b
   return a
       
def main():
  n1 = eval(input("Enter num1:"))
  n2 = eval(input("Enter num2:"))
  print(gcd(n1,n2))

if __name__=='__main__':
    main()