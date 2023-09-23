isSuccess = False

def stuff():
    try:
        isSuccess = False
        return("return from try")
    except:
        isSuccess = True
        return "return from except"
    finally:
        if isSuccess:
            print("printed from finally block")
        else:
            print("wasn't success do nothing")
# x = stuff()
# print(x)

def new(a,b,c=None):
    if c is None:
       print(a+b)
    else:
       print(a+b+c)

new(2,3,7)