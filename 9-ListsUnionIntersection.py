def union(l1,l2):
    union_list = []
    for x in l1:
       if x not in union_list:
            union_list.append(x)
       for y in l2:
          if y not in union_list:
            union_list.append(y)
    union_list.sort()
    return union_list
    
def intersection(l1,l2):
    intersection_list =[]
    for x in l1:
        for y in l2:
           if y==x:
              if y not in intersection_list:
                 intersection_list.append(y)  
    intersection_list.sort()             
    return intersection_list

def non_intersection(l1,l2):
    non_intersection_list=[]
    l1.sort()
    l2.sort()
    
    for x in l1:
       if x not in l2 and x not in non_intersection_list:
          non_intersection_list.append(x)
    for y in l2:
       if y not in l1 and y not in non_intersection_list :
          non_intersection_list.append(y)
    
    non_intersection_list.sort()
    return non_intersection_list          
                            
def main():
   l1=eval(input("Enter list1: "))
   l2=eval(input("Enter list2: "))
   union_list= union(l1,l2)
   intersection_list = intersection(l1,l2)
   non_intersection_list=non_intersection(l1,l2)
   print("Union of two lists is:{0}".format(union_list))
   print("Intersection of two lists is:{0}".format(intersection_list))
   print("Non-Intersection of two lists is:{0}".format(non_intersection_list))

if __name__=='__main__':
    main()
    