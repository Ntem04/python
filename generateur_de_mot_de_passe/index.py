#utf-8

import random
import string 


def generate_password(min_length,numbers=True,special_charactere=True):
    
    letters = string.ascii_letters
    digit = string.digits
    special = string.punctuation
    
    characters = letters
    if  numbers :
        characters += digit
    if  special_charactere:
        characters += special
        
        
    pwd = ""
    meets_criteria = False
    has_special = False 
    has_numbers = False
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        
        if new_char in digit:
            has_numbers = True
        elif new_char in special:
            has_special = True
            
            
        meets_criteria = True
        
        if numbers:
            meets_criteria = has_numbers
        if special_charactere:
            meets_criteria = meets_criteria and has_special
    print(pwd)


 
            
generate_password(10,False,False)            
    
        