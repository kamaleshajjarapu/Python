def count_lines_words_chars(filename):
    fd=open(filename,'r')
    count_lines=0
    count_words=0
    count_chars=0
    lines=fd.readlines()
    print(lines)
    for line in lines:
        words=[]
        count_lines+=1
        words=line.split()
        for word in words:
            count_words+=1
            count_chars+=len(word)
    fd.close()
    return (count_lines,count_words,count_chars)

def longest_line(filename):
    fd=open(filename,'r')
    lines=fd.readlines()
    #print(len(lines))
    max=len(lines[0].strip())
    max_line=lines[0]
    for i in range(1,len(lines)):
        if len(lines[i].strip())>max:
            max=len(lines[i])
            max_line=lines[i]
                
    print('Longest line is: %s' %(max_line)) 

def LongestShortestLine(filename):
    fd=open(filename)
    if fd!=None:
        line=fd.readline()
        max_line=line
        min_line=line
        while line!='':
            line=fd.readline()
            if line=='':
                break
            if len(line)>len(max_line):
                max_line=line
            if len(line)<len(min_line):
                min_line=line
    return min_line,max_line
def main():
    filename=eval(input("Enter a filename:"))
    count_lines,count_words,count_chars=count_lines_words_chars(filename)
    longest_line(filename)
    print('Total num of lines in the file:%d'%(count_lines))
    print('Total num of words in the file:%d'%(count_words))
    print('Total num of chars in the file:%d'%(count_chars))
    
if __name__=='__main__':
    main()
    