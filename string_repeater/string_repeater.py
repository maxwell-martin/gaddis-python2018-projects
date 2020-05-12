def repeat(aString, anInt):
    result = ""
    for i in range(anInt):
        result += aString
    return result

print(repeat("Hello", 5))

