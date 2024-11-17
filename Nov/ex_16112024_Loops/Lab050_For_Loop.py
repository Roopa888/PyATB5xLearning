#For loop-->Repat a blcok of code multipel times

#To rpint "Hello Word" 10 times
#syntax -->range(start ,stop-1)-->if we give to print in range (1,10) ,actually it prints from 1 to (10-1) i.e 1 to 9
#Means 9 times it will print but the iteration actaully strats from 1 and goes on till 9 and not 10
#if you want to print 10 times you have to give the start point as range(0,10)
for i in range(1,10):
    print("Hello World")
    for i in range(1, 10):
        print(i)