def lists_compare(L1,L2):
    #print(L1)
    count=0
    if len(L1)==len(L2):
       L1.sort()
       L2.sort()
       for i in range(0,len(L1)):
          #print(i)
          if L1[i]==L2[i]:
            count+=1
    else:
       print("Both lists are not same")      
       
    if count==len(L1):
       print("Both lists are same")
    else:
       print("Both lists are not same")      



if __name__=="__main__":
    L1=eval(input("Enter list1:"))
    L2=eval(input("Enter list2:"))
    lists_compare(L1,L2)