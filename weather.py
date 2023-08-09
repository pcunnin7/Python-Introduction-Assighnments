NAME = 1
SNWD = 9
TAVG = 10
TMAX = 11

def loadData():
    '''
open the weather file data to read
    '''
    file = open("2466150.csv", mode = 'r')
    counter = 0
    header = file.readline()
    tokens = header.split(',')
    print(tokens[1],tokens[2],tokens[8],tokens[9],tokens[10])
    
    for line in file:
        tokens = line.split(',')
        if len(tokens[1]) == 0 or \
           len(tokens[SNWD]) == 0 or \
           len(tokens[TAVG]) == 0 or \
           len(tokens[TMAX]) == 0:
            continue
        
        name = tokens[1]
        snowOnTheGround = float(tokens[SNWD][1:-1])
        avgTemp = float(tokens[TAVG][1:-1])
        maxTemp = float(tokens[TMAX][1:-1])
        print(name, snowOnTheGround,avgTemp,maxTemp)
        
   
        if counter > 10:
            break
        counter += 1


if __name__ == '__main__':
    loadData()
