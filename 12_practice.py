# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>'''
l1 = letter.replace("<|Name|>", "John").replace("<|Date|>", "1/1/2023")
print(l1)
