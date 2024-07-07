class Error(Exception):
    """Base class for other excptions"""
    pass 
class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass 
class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass 


while True:
    
    try:
        number = int(input('enter number: '))
        if number < 6:
            raise ValueTooSmallError
        elif number > 6:
            raise ValueTooLargeError 
        break 
    except ValueTooLargeError:
        print("this value too large ")
    except ValueTooSmallError:
        print("this value too small") 
        
print("congratulations! You guessed it correctly")        


print("---------another one------------")


class Error(Exception):
    pass 

class intChecker(Error):
    pass 
class stringChecker(Error):
    pass 

while True:
    try:
        ab = input("int : ")
        bc = input("eer : ")

        if not ab.isdigit():
            raise intChecker
        elif not bc.isalpha():
            raise stringChecker
        break
    except intChecker:
        print("your given value is not int")
    except stringChecker:
        print("your input not string")
        
    except ValueError:
        print("invalid input")