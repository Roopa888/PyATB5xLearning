# pass is a placeholder statement which does nothing
# used when syntactically required but no action is needed
for i in range(0, 10, 1):  # --->loop 9 times
    if i == 6 or i == 5:
        print(i)
    else:
        pass
# |i|condition              | Output|
# |0|0==6 or 0==5->False   |pass-Nothing will be printed|
# |1|1==6 or 1==5->False   |pass -Nothing will be printed|
# |2|2==6 or 2==5->False   |pass -Nothing will be printed|
# |3|3==6 3==5->False       |pass -Nothing will be printed|
# |4|4==6 or 4==5->False    |pass -Nothing will be printed|
# |5|5==6 or 5==5->True     |5|
# |6|5==6 or 6==5->True     |6|
# |7|7==6 or 7==5->False    |pass -Nothing will be printed|
# |8|8==6 or 8==5->False    |pass -Nothing will be printed|
# |9|9==6 or 9==5->False    |pass=-Nothing will be printed and exit the For loop|
