def from_keys(employee_dict,value=None):
   #print(d)
   #print(value)
   d={}
   i=0
   
   for key in employee_dict:
      if i<len(value):
        d[key]=value[i]
      else:
        d[key]=None 
      i+=1
   if len(value)>len(d):
    d[key]=value[i:]
   print(d)
   '''
   length=len(employee_dict)
   for key in employee_dict:
      if i+1==length and i+1!=len(value):
        d[key]=value[i:]
      elif i<len(value):
        d[key]=value[i]
        i+=1
      else:
        d[key]=None
   '''   
   print(d)          
def main():
   employee_dict = {'Name':'Krishna','Age':30,'Org':'QLogic'}
   #d=dict.fromkeys(employee_dict)
   l1=['Kamalesh',30,'QLogic']
   l2=['Kamalesh']
   l3=['Kamalesh',30,'QLogic','Dharma',32,'QLogic']
   from_keys(employee_dict,l1)
   from_keys(employee_dict,l2)
   from_keys(employee_dict,l3)
if __name__=='__main__':
    main()
    