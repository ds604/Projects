import sys

def reverse_string(str):
    return str[::-1]
    
if __name__=="__main__":
    try:
        args = sys.argv
        print reverse_string(args[1])
    except:
        print "Enter a string to reverse."
