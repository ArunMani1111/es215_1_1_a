#function to determine which day of the week has the date '1'
def fday(m,y):
    k=y-1
    p=k//4 - k//100 + k//400
    q=(k+p)%7
    l=0
    if (y%4==0 and y%100!=0) or y%400==0:
        if m=='jan':
            l=0
        elif m=='feb':
            l=3
        elif m=='mar':
            l=4
        elif m=='apr':
            l=0
        elif m=='may':
            l=2
        elif m=='jun':
            l=5
        elif m=='jul':
            l=0
        elif m=='aug':
            l=3
        elif m=='sep':
            l=6
        elif m=='oct':
            l=1
        elif m=='nov':
            l=4
        elif m=='dec':
            l=6
    else:
        if m=='jan':
            l=0
        elif m=='feb':
            l=3
        elif m=='mar':
            l=3
        elif m=='apr':
            l=6
        elif m=='may':
            l=1
        elif m=='jun':
            l=4
        elif m=='jul':
            l=6
        elif m=='aug':
            l=2
        elif m=='sep':
            l=5
        elif m=='oct':
            l=0
        elif m=='nov':
            l=3
        elif m=='dec':
            l=5
    return (l+q)%7
#function to decide number of days in the month
def md(m,y):
    if m=='jan' or m=='mar' or m=='may' or m=='jul' or m=='aug' or m=='oct' or m=='dec':
        return 31
    elif m=='apr' or m=='jun' or m=='sep' or m=='nov':
        return 30
    elif m=='feb' and ((y%4==0 and y%100!=0) or y%400==0):
        return 29
    else:
        return 28
# main code
ans='y'
while(ans=='y'):
    print("______________CALENDAR___________________")
    print("Enter the first three letters of the month: ", end=' ')
    d = [[0 for x in range(7)] for y in range(6)]
    month = input()
    month = month.lower()
    print("Enter the year(YYYY): ", end=' ')
    year = int(input())
    print(month, "    ", year)
    print("MON TUE WED THU FRI SAT SUN")
    a = fday(month, year)
    for i in range (0,6):
        for j in range (0,7):
            d[i][j] = 0
    d[0][a] = 1
    b = 2
    c = md(month, year)
    for i in range(0,6):
        for j in range (0,7):
            if i!=0 or j>a:
                d[i][j] = b
                b+=1
            if b>c:
                break
    for i in range (0,6):
        for j in range (0,7):
            if d[i][j]==0:
                print("   ", end=" ")
            elif d[i][j]//10==0:
                print(" ", d[i][j], end=" ")
            elif d[i][j]<=c:
                print("", d[i][j], end=" ")
        print(end='\n')
    print("do you wish to continue?(y/n)")
    ans=input()












