# For loop with break condition within
for i in range(0, 10):
    print(i)  # print 0 to 9 .Loop executes 10 times
    if i == 5:
        break

# |i|condition|Output|
# |0|0==5-->False|0|
# |1|1==5-->False|1|
# |2|2==5-->False|2|
# |3|3==5-->False|3|
# |4|4==5-->False|4|
# |5|5==5-->True|break out of For loop|
