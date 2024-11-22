# For loop actual syntax(for in range(start,stop,step):
# start-depends on the value you give 1 or 0.Give 1 ---->will print 10-1 times ,Give 0--->will print 10 times
# stop--->stop-1 eg:10 --->10-1=9(9 times)
# step-the increment step if we don't give it in range like eg:for in range(1,10)
# step will be 1 by default like below
for i in range(0, 10):
    print(i)
#suppose if we want to make the increment by 2 in For loop ,we have to give the step value as 2
# Then the above program will just print the values incremented by 2
#Also in the below code ,the start value is zero .So it will add 2 steps starting with zero unlike the above For loop
print("Increment step by 2")
print("---------------")
for i in range(0, 10,2):
    print(i)