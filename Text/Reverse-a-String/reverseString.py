import sys

def reverse_string(str):
    return str[::-1]
    
if __name__=="__main__":
    try:
        args = sys.argv
        first_arg = str(args[1])
        print reverse_string(first_arg)
    except:
        print "Enter a string to reverse."
