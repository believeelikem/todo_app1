import re 
import string

# print(string.punctuation)

def is_strong(password):
    
    if len(password) < 8:
        return False        
    
    letters = string.ascii_letters
    numbers = string.digits
    characters = string.punctuation
    
    for character_set in (letters,numbers,characters):
        if not re.search(f'[{character_set}]',password):
            return False
        
    return True

    

print(is_strong("A2344444a!"))
    