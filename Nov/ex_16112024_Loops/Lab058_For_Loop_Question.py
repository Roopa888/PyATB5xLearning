for i in range(0, 10, 1):  # --->loop 9 times
    if i == 6:
        print(i)
    else :
                print("No Output")
    # |i|condition     | Output|
    # |0|0==6->False   |No Output|
    # |1|1==6->False   |No Output|
    # |2|2==6-->False |No Output|
    # |3|3==6-->False |No Output|
    # |4|4==6-->False |No Output|
    # |5|5==6-->False |No Output|
    # |6|6==6-->True |6       |
    # |7|7==6-->False |No Output|
    # |8|8==6-->False |No Output|
    # |9|9==6-->False |No Output-and also exit the loop as the stop value has reached|
