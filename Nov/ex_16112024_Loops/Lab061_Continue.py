# continue statement skips the current iteration of a loop and moves to the next iteration.
# differnce between pass and continue is
# pass can be used in the statement ,functions ,objects and classes also (will see in later sessions)
for number in range(10): # iterates from 0 to 9 (10 times)
    if number%2==0:
        continue
    else:
        print(number)


# |i|condition                      | Output|
# |0|0%2 ==0->True                  |Nothing will be printed|
# |1|1%2 ==0->False                 |1|
# |2|2%2 ==0->True                  |Nothing will be printed|
# |3|3%2 ==0->False                  |3|