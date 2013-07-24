import sys

def reverse_string(str):
    return str[::-1]
    
if __name__=="__main__":
    try:
        input = raw_input("Enter a string: ")
        input = str(input)
        print reverse_string(input)
    except:
        print "Enter a string to reverse."
