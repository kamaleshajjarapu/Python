def not_bad(input_str):
    not_index=input_str.find('not') 
    bad_index=input_str.find('bad')
    replace_by='good'
    #print(not_index)
    #print(bad_index)
    return (input_str.replace(input_str[not_index:bad_index+3],replace_by))
def main():
  input_str = eval(input("Enter a string with \"not bad\": " ))
  print(not_bad(input_str))

if __name__=='__main__':
  main()