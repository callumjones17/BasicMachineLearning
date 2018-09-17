
def getNum(prompt,errorPrompt):
    """Get a number from the user, prints errorPrompt if input is not an Integer type"""
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