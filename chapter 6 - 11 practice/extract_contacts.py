import re

text_example ="""Hi Team,

Please contact Alice at alice.smith+project@example.com or on her US line (415) 555-4242 ext. 321.  
For UK support, email support-uk@company.co.uk or call +44 20 7946 0958.  

Bob's direct line is 212.555.7890, and you can also try Carol at carol99@sample.org.  
Our old number was 0044 161 496 0999 #77, but that line is being retired.  

Note: IDs like 123-45-6789 and dates like 05-12-2024 should NOT be mistaken for phone numbers.  

Thanks,  
The Support Team"""



def extract_contacts(text: str):
    email_pattern = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', re.IGNORECASE) #Username, Domain, TLD
    us_phone_pattern = re.compile(r'(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})(?:\s*(?:ext|x|#)\s*\d{2,5})?', re.IGNORECASE)
    uk_phone_pattern = re.compile(
        r'(?<!\d)(?:(?:\+44|0044)[\s.-]?(?:7(?:[\s.-]?\d){9}|[12](?:[\s.-]?\d){9})|0(?:7(?:[\s.-]?\d){9}|[12](?:[\s.-]?\d){9}))(?:\s*(?:ext\.?|extension|x|#)\s*\d{2,5})?(?!\d)', re.IGNORECASE
    )
    #I'll be honest i just copied and pasted the patterns

    emails = [m.group(0) for m in email_pattern.finditer(text)]
    phones = [m.group(0) for m in us_phone_pattern.finditer(text)] + [m.group(0) for m in uk_phone_pattern.finditer(text)]


    return {"emails": emails, "phones": phones}



example = extract_contacts(text_example)

print(example)

 