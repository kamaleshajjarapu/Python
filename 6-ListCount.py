def list_count(l1,key):
    count=0
    for x in l1:
       if key==x:
          count+=1
    return count  
 
if __name__=='__main__':

    l1=eval(input('Enter a list:'))
    key=eval(input('Enter a list member\'s count to be calculated:'))
    print(list_count(l1,key))