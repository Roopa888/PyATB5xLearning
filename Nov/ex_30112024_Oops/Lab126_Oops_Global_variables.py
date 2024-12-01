# working of global variable
count=0
def increment():
    global count
    count=count+1 # cannot directly access a here without "global count" dec  @UnboundLocalError: cannot access local variable 'count' where it is not associated with a value


increment()
increment()
increment()
increment()
print(count)