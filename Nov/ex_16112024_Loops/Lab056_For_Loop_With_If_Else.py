# For loop with if ..else condition within
for i in range(0, 10):  # print 0 to 9 .Loop executes 10 times
    if i == 5:
        print("Five")
    else:
        print(i)

#|i|condition|Output|
#|0|0==5-->False|0|
#|1|1==5-->False|1|
#|2|2==5-->False|2|
#|3|3==5-->False|3|
#|4|4==5-->False|4|
#|5|5==5-->True|Five|
#|6|6==5-->False|6|
#|7|7==5-->False|7|
#|8|8==5-->False|8|
#|9|9==5-->False|9|
#|10|10==5-->False|exit the For loop and it reached the stop value.