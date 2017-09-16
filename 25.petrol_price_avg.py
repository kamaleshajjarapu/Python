def price_avg(filename):
    fd=open(filename)
    if fd!=None:
        lines=fd.readlines()
        states=[]
        curr_monthly_price=[]
        prev_month_price=[]
        first_month_flag=True
        count=0
        
        states = lines[0].split()
        for i in range(1,len(lines)):
            total_price=[]
            count+=1 # To count no of months for avg
            curr_monthly_price = lines[i].split()
            print(curr_monthly_price)
            if first_month_flag:
                for j in range(1,len(curr_monthly_price)):
                    prev_month_price.append(int(curr_monthly_price[j]))  # Taking first month's price of each state as prev_month_price
                first_month_flag=False   
                continue    
            for j in range(1,len(curr_monthly_price)):
                sum = prev_month_price[j-1]+int(curr_monthly_price[j]) 
                total_price.append(sum)
            prev_month_price=total_price
        return(states[1:],total_price,count)
        
def main():
    filename=r'C:\pythonprogs\2017\Petrol.txt'
    states,total_price,count=price_avg(filename)
    for i in range(0,len(states)):
        avg= total_price[i]/count
        print("Avg petrol price of {0} is {1}".format(states[i],avg))
if __name__=='__main__':
    main()