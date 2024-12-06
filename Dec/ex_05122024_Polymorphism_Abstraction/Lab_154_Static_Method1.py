# Static methids belongs to a class rather than teh instance of a class
# can be called using the class name without creating the class
class o:
    @staticmethod
    def sum(a,b):
        return a+b

    def diff(self,a,b):
        return a-b

print("Static method without creating the object",o.sum(2,9))
# print("Non static method without creating the object",o.diff(12,4)) # will give error
print("Non static method without creating the object",o().diff(12,4)) # we have to create an object and call teh function
