import random
import string
from Four import Four_Numbers

def Generate_Password(length):
    if length < 8:
        return 'size must be at least 8!'
        
    ls = Four_Numbers(length)
    len_low= ls[0]
    len_up = ls[1]
    len_num = ls[2]
    len_sym = ls[3]
        
    S = ''
    
    # upper_case letters
    random_up = ''.join(random.choices(string.ascii_uppercase, k=len_up))
    S += random_up
    
    # lower_case_letters
    random_low = ''.join(random.choices(string.ascii_lowercase, k=len_low))
    S += random_low
    
    #numbers
    random_num = [random.randint(0, 9) for _ in range(len_num)]
    S += ''.join(str(x) for x in random_num)
    
    #symbols
    random_sym = ''.join(random.choices(string.punctuation, k=len_sym))
    S += random_sym
    
    char_list = list(S)
    random.shuffle(char_list)
    shuffled = ''.join(char_list)
    
    return shuffled

print(Generate_Password(12))