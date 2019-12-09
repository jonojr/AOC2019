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

    smallestZerosCount = layerSize
    smallestZerosLayer = 0

    for layer in layers:
        numZeros = layer.count(0)

        if numZeros < smallestZerosCount:
            smallestZerosCount = numZeros
            smallestZerosLayer = layer
    
    print(smallestZerosLayer.count(1) * smallestZerosLayer.count(2))
    printLayer(smallestZerosLayer)
