# A lambda is an anonymous function that returns some form of data.
# def num_pow(num):
#        return num**3
# result=num_pow(2)
# print(result)

result1 = lambda num: num ** 3  # lambda returns a function object.ie num_pow(2) is equal to lambda num:num**4
print(result1(2))
