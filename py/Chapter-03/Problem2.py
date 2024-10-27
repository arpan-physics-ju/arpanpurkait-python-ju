letter = ''' Dear <|NAME|>,
You are selected!
<|DATE|>'''

name = "Arpan Purkait"

print(letter.replace("<|NAME|>",name).replace("<|DATE|>","27-10-2024"))