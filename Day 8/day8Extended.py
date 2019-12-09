width = 25
height = 6

def printLayer(layer):
    for i in range(height):
        startPosition = i * width
        endPosition = (i + 1) * width
        print(layer[startPosition:endPosition])

if __name__ == "__main__":

    layerSize = width * height
    data = None
    with open("input.txt", 'r') as f:
        data = f.read()
        data = [int(x) for x in data]
    
    numLayers = len(data) / layerSize
    layers = []

    for i in range(int(numLayers)):
        startPosition = i * layerSize
        endPosition = (i + 1) * layerSize
        layers.append(data[startPosition:endPosition])

    result = layers[-1]
    for i in range(1, int(numLayers) + 1):
        newLayer = layers[-1 * i]
        for j in range(layerSize):
            if newLayer[j] == 1:
                result[j] = 1
            elif newLayer[j] == 0:
                result[j] = 0
    printLayer(result)
    print('\n\n')
    print(result)

