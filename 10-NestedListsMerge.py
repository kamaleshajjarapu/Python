def nested_to_single_list(l1,l2):
   #l2=[]
   for x in l1:
      #print(x)
      if type(x)==list:
        nested_to_single_list(x,l2)
      else:
        l2.append(x)
   return l2
def main():
   l1=eval(input("Enter a nested list: "))
   l2=[]
   l2=nested_to_single_list(l1,l2)
   print(l2)
if __name__=='__main__':
   main()