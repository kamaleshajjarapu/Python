#!C:\Users\kajjarapu\AppData\Local\Programs\Python\Python36-32\python.exe

def SumUntilZero():
    result =0
    while(1):
      n = eval(input("Enter a number:"))
      if n==0:
        print("You entered zero")
        break
      result+=n
    print(result)

if __name__ == '__main__':
   
   SumUntilZero()