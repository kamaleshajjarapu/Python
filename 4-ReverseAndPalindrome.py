
def reverse(num):
    n=num
    reverse=0
    remainder=0
    while n!=0:
       remainder=n%10
       reverse = reverse*10+remainder
       n = n//10
    return reverse
def palindrome(n):
    rev=reverse(n)   
    if n==rev:
       print("{0} is palindrome".format(n))
    else:
       print("{0} is not palindrome".format(n))
def main():
    num = eval(input("Enter num:"))
    print(reverse(num))
    palindrome(num)
if __name__=='__main__':
    main()