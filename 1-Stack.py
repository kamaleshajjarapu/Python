def push(stack_list,maxsize,element):

   if len(stack_list)==maxsize:
       print("Stack is full" + '\n')
       return                  
   stack_list.append(element)
   
      
def pop(stack_list,element):
    if len(stack_list)==0:
       print("Stack is empty" + '\n')
       return
    element=stack_list.pop()
    print("{0} has been popped out successfully".format(element) + '\n')
    

def display(stack_list):
    if len(stack_list)!=0:
       print("Current stack is: {0}".format(stack_list) + '\n')     
    else:
       print("Stack is empty")
       
def main():
   stack_list = []
   maxsize = 5
   while True:
       print('\n' + 'Stack operations:' + '\n')
       print('1: Push' '\n')
       print('2: Pop' '\n')
       print('3: Display' '\n')
       print('4: Exit' '\n')
       input_val = eval(input("Enter your input: "))
       if input_val==1:
          element = eval(input("Enter the element to be pushed into the stack: "))
          push(stack_list,maxsize,element)
       if input_val==2:
          #element = eval(input("Enter the element to be popped out of the stack:")) 
          pop(stack_list,element)
       if input_val==3:
          #element = eval(input("Enter the element to be popped out of the stack:")) 
          display(stack_list)
       if input_val==4:
          exit()

if __name__=='__main__':
   main()
