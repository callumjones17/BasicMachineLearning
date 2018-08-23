

def clamp(input, clamp):
    """Clamps a value to a specific Maximum"""
    output = input
    if input > clamp:
        output = clamp
    return output

def clampR(input, clampMax, clampMin):
    """Clamps a value to a specific range"""
    output = input
    if input > clampMax:
        output = clampMax
    elif input < clampMin:
        output = clampMin
    return output

def makeEven(input):
    """Ensures a number is Even, adds 1 if not"""
    output = input
    if output%2 == 0:
        return output
    else:
        return output +1

def clampArray(array,clamp):
    """Clamps number of elements in an array"""
    outArray = []
    for i in range(0,clamp):
        outArray.append(array[i])
    return outArray

def clampEx(num,avoid):
    if num == avoid:
        num += 1
    return num
