import re

def strong_password(password: str) -> tuple[bool, str]:
    if not isinstance(password, str):
        raise TypeError("Input must be a string")
    
    if len(password) < 8:
        return False, "Password must be longer than 8 characters"
    
    
    pattern_whitespace = re.compile(r'\s')
    if pattern_whitespace.search(password):
        return False, "Password must not contain whitespaces"


    #Detect uppercase and lowercase in the password
    pattern_uppercase = re.compile(r'[A-Z]')
    pattern_lowercase = re.compile(r'[a-z]')

    if not pattern_lowercase.search(password) or not pattern_uppercase.search(password):
        return False, "Password must contain both lowercase and uppercase"
    

    pattern_specialcharacter = re.compile(r'[^A-Za-z0-9]')

    if not pattern_specialcharacter.search(password):
        return False, "Password must contain a special character"
    

    return True
    
"""
 import re

def strong_password(password: str) -> tuple[bool, str]:
    if not isinstance(password, str):
        raise TypeError("Input must be a string")
    
    if len(password) < 8:
        return False, "Password must be longer than 8 characters"
    
    if re.search(r'\s', password):
        return False, "Password must not contain whitespaces"
    
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    
    if not re.search(r'[^A-Za-z0-9]', password):
        return False, "Password must contain at least one special character"
    
    return True, "Password is strong"
 
 """


    

        
    
