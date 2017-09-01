def string_rotate(input_str,rotation_str):
    if len(input_str)!=len(rotation_str):
       return False
    return rotation_str in input_str+input_str       

def RotateString(first_str,validate_str):
    if len(first_str)!=len(validate_str):
       return False
    str_list=[]
    temp_str=first_str
    while True:
        temp_str=temp_str[-1]+temp_str[:len(temp_str)-1]
        str_list.append(temp_str)
        print(temp_str)
        if temp_str==first_str:
          break
    print("All possible rotated combinations of input string is {}".format(str_list))
    return validate_str in str_list
def main():
   input_str=eval(input("Enter a string: "))
   rotation_str=eval(input("Enter rotation string:"))
   if string_rotate(input_str,rotation_str) and RotateString(input_str,rotation_str):
      print('True')
   else:
      print('False')
if __name__=='__main__':
   main()