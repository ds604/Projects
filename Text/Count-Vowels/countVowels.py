import sys

def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    i = 0
    for letter in s:
        if letter in vowels:
            i += 1
    return i

def count_vowels_fn(s):
    vowels              = ['a', 'e', 'i', 'o', 'u']
    vowel_mask          = [1 if letter in vowels else 0 for letter in s]
    number_of_vowels    = sum(vowel_mask)
    return number_of_vowels
    
if __name__=="__main__":
    try:
        input_string = str(sys.argv[1])
        print count_vowels(input_string)
    except:
        print "Enter a string to count vowels."
