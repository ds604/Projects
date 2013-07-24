import sys

def count_vowels(s, method="imperative"):
    def count_vowels_imperative(s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        i = 0
        for letter in s:
            if letter in vowels:
                i += 1
        return i
    
    def count_vowels_functional(s):
        vowels              = ['a', 'e', 'i', 'o', 'u']
        vowel_mask          = [1 if letter in vowels else 0 for letter in s]
        number_of_vowels    = sum(vowel_mask)
        return number_of_vowels
    
    pager   = {"imperative": count_vowels_imperative, 
                "functional": count_vowels_functional}
    result  = pager[method](s)
    return result

    
if __name__=="__main__":
    try:
        arguments = sys.argv
        if len(arguments) == 1:
            raise
        elif len(arguments) == 2:
            input_string = str(arguments[1])
            print "default"
            print count_vowels(input_string)
        elif len(arguments) == 3:
            input_string    = str(arguments[1])
            method_type     = str(arguments[2])
            print method_type
            print count_vowels(input_string, method=method_type) 
        else:
            raise
    except:
        print "Enter a string to count vowels."
