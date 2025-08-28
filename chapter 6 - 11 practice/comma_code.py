def comma_code(items):
    if not items:
        return ''
    
    elif len(items) == 1:
        return str(items[0])
    

    return ', '.join(items[:-1]) + " and " + items[-1]