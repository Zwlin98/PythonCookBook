# Create by Zwlin
import re
text = 'UPPER PYTHON, lower python, Mixed Python'

res = re.findall(r'python',text,flags=re.IGNORECASE)

print(res)

res = re.sub('python','snake',text,flags=re.IGNORECASE)

print(res)

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace

text = 'UPPER PYTHON, lower python, Mixed Python'

res = re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)
# UPPER SNAKE, lower snake, Mixed Snake