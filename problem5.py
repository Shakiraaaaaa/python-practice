letter='''
name : <|Name|>
date : <|DATE|>
'''
name=input("enter your name : ")
date=input("enter date : ")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)