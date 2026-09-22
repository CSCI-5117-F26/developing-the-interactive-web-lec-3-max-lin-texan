def twice(somefunc):
    def inner(*args, **kwargs):
        somefunc(*args, **kwargs)
        somefunc(*args, **kwargs) 
    
    return inner 

@twice
def saymoo():
    print("moo")

saymoo()