def pattern1(n):
    for i in range(1,n+1):
       for j in range(1,i+1):     
           #print(j,end='')
           print('*\t',end='')
       print('\n')

def pattern2(n):
    for i in range(n,0,-1):
        for j in range(i):
            print('*\t',end='')
        print('\n')
       
def pattern3(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print("\t",end='')
        for k in range(i):
            print("*\t",end='')
        print('\n')

def pattern4(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print("\t",end='')
        for k in range(0,2*i+1):
            print("*\t",end='')
        print('\n')
        
def pattern5(n):
    for i in range(n,0,-1):
        for j in range(0,n-i):
            print('\t',end='')
        for k in range(2*i-1,0,-1):
            print('*\t',end='')
        print('\n') 
        
        
                 
        
        
def patternABC1(n):
    for i in range(1,n+1):
        for c in range(65,65+i):
            print('%c '%c,end='') 
        print('\n')

def patternABC2(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print('\t',end='')  
        for c in range(65+i,64,-1):
            print('%c\t' %c,end='')
        for c in range(66,66+i):
            print('%c\t' %c,end='')
        print('\n')
        
    
        
def main():
    n=eval(input('Enter no of rows to print pattern:'))
    pattern1(n)
    print('\n')
    pattern2(n)
    print('\n')
    pattern3(n)
    print('\n')
    pattern4(n)
    print('\n')
    pattern5(n)
    print('\n')
    patternABC1(n)
    print('\n')
    patternABC2(n)
    
if __name__=='__main__':
    main()
    