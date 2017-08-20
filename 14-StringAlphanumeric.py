def AddNumInString(input_str):
   sum=0
   for i in input_str:
      #print(i)
      if i.isnumeric():
        sum+=int(i)
   return sum        
def main():
   input_str = eval(input("Enter an alpha-numeric string: "))
   print(AddNumInString(input_str))
   
if __name__=='__main__':
   main()
   