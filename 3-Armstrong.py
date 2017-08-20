def sum_of_cubes_digits(num):
    list_digits = []
    value = 0
    if num//10==0: 
       return num
    while num!=0:
       list_digits.append(num%10)
       num = num//10
    for n in list_digits:
       value = value + n**3
    return value
def armstrong(num):
    res = sum_of_cubes_digits(num)
    if res==num:
      print("{0} is an armstrong number".format(num))
    else:
      print("{0} is not an armstrong number".format(num))

def main():
    num = eval(input("Enter a number to check whether it is armstrong or not: "))
    sum_of_cubes_digits(num)
    armstrong(num)

if __name__=='__main__':
    main()
    