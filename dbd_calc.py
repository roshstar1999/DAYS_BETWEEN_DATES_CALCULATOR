def LeapYearCount(D):
    #to check if current year needs to be considered or not as a leap year
    years=D[2]
    
    if (D[1]<=2):# if Feb or Jan
        years-=1
        
    
    #a year is leap if multiple of 4 ,multiple of 400 and not 100,
    res=years//4
    res-=years//100
    res+=years//400
    
    return res

def DaysFromZero(D):
    month=[31,28,31,30,31,30,31,31,30,31,30,31]
    def monthdays(x):
        if x==1:
            return 0
        else:
            return(sum(month[:x-1]))
        
    
    
    result=365*D[2]+LeapYearCount(D)+monthdays(D[1])+D[0]
    return result
def Difference(D1,D2):
    a=DaysFromZero(D1)
    b=DaysFromZero(D2)
    #for inc last date
    if a>b:
        return(a-b+1) 
    else:
        return (b-a+1)
    
def main():
    print("HI! THIS IS NO. OF DAYS BETWEEN ANY TWO DATES CALCULATOR")
    print("ENTERING FIRST DATE.....")
    
    t1=[int(i) for i in input("enter d/m/y").split("/")]
    print()
    print("ENTERING SECOND DATE.....")
    t2=[int(i) for i in input("enter d/m/y").split("/")]
    print()
    
    print("the no. of days in between are",Difference(t1,t2))
    
main()   
    
