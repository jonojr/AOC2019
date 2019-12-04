def isOK(number):
    strNum = str(number)
    previous = None
    occurences = {}
    for i in range(len(strNum)):
        if previous and previous > strNum[i]:
            return 0
        
        if strNum[i] in occurences.keys():
            occurences[strNum[i]] += 1
        else:
            occurences[strNum[i]] = 1
        
        previous = strNum[i]
    
    for key in occurences.keys():
        item = occurences[key]
        if item >= 2:
            return 1
    return 0

def isExtensionOK(number):
    strNum = str(number)
    previous = None
    occurences = {}
    for i in range(len(strNum)):
        if previous and previous > strNum[i]:
            return 0
        
        if strNum[i] in occurences.keys():
            occurences[strNum[i]] += 1
        else:
            occurences[strNum[i]] = 1
        
        previous = strNum[i]
    
    for key in occurences.keys():
        item = occurences[key]
        if item == 2:
            return 1
    return 0

if __name__ == "__main__":
    
    min = 146810
    max = 612564

    count = 0
    extensionCount = 0

    for i in range(min, max + 1):
        count += isOK(i)
        extensionCount += isExtensionOK(i)

    print(f"Passwords: {count}\nExtension Passwords: {extensionCount}")