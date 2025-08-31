import re

def new_strip(text: str, chars: str = None)->str:
    if chars is None:
        return re.sub(r'^\s+|\s+$', "", text)
    
    else:

        return re.sub(rf'^[{re.escape(chars)}]+|[{re.escape(chars)}]+$', "", text)