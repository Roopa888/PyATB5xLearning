for i in range(1,101):# if we start from zero it will print zero also upto 100 ,if we start with1 it will print 2 to 100 even numbers
    if i % 2 == 0:
        print(i)

        # |i|condition              | Output|
        # |0|0%2 ==0->True          |0|
        # |1|1%2==0->False          |Nothing will be printed|
        # |2|2%2==0 ->True             |2|
        # |3|3%2==0-->False            |Nothing will be printed|
        # |4|4%2==0-->True              |4|
