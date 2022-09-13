from math import trunc
computerInStock = {"msiRtxa5000": 4199.35, "gigabyteAero": 4295.54, "razerblade15": 3696.99, "asuszephyrus": 1849.79}
def lowestPrice():
    return min(computerInStock, key=computerInStock.get)
def highestPrice():
    return max(computerInStock, key=computerInStock.get)
def getRoundedPrice():
    valueList = []
    computerList = list(computerInStock.keys())
    for i in range(len(computerList)):
        value = computerInStock[computerList[i]]
        valueList.append(value)
    numberOfItems = len(valueList)
    for x in range(numberOfItems):
        number = valueList.pop(0)
        roundedNumber = round(number)
        valueList.append(roundedNumber)
    print(f"The rounded Price for the MSI RTXa 5000 is: {valueList[0]}")
    print(f"The rounded Price for the Gigabyte Aero is: {valueList[1]}")
    print(f"The rounded Price for the Razer Blade 15 is: {valueList[2]}")
    print(f"The rounded Price for the Asus Zephyrus is: {valueList[3]}")
def getAveragePrice():
    valueList = []
    computerList = list(computerInStock.keys())
    for i in range(len(computerList)):
        value = computerInStock[computerList[i]]
        valueList.append(value)
    numberOfItems = len(valueList)
    return print(f"The rounded price of all the laptops is: {trunc(sum(valueList)/numberOfItems)}")



print(lowestPrice())
print(highestPrice())
# print(roundPrice())
getRoundedPrice()
getAveragePrice()