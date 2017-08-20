def bubble_sort(l1):
   count = 1
   while count:
      count=0
      for i in range(0,len(l1)-1):
          if l1[i]>l1[i+1]:
             l1[i],l1[i+1]=l1[i+1],l1[i]
             count+=1
             continue
    
   return l1
def main():
   l1=eval(input("Enter an unsorted list: "))
   l1=bubble_sort(l1)
   print(l1)
if __name__=='__main__':
   main()
   