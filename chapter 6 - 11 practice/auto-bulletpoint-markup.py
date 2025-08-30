import pyperclip

text = pyperclip.paste()

split_text = text.split('\r\n')

new_string = []
for i in split_text:
    new_string.append('* ' + i)

final_string = "\r\n".join(new_string)

pyperclip.copy(final_string)

#There can be many improvements made here, such as the existent of copying empty lines