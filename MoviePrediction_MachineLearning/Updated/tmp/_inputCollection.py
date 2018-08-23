
def getNum(prompt,errorPrompt):
    validData = False
    while validData == False:
        num = input(prompt)
        try:
            num = int(num)
        except ValueError:
            print(errorPrompt)
        else:
            validData = True
    return num