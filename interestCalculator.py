
def calculateFutureBalance(amountPerMonth, rate, yearsSaved):
    total = 0
    for month in range(yearsSaved * 12):
        total = total + total * rate + amountPerMonth
        
    return total

def main():
    savePerMonth = int(input("How much will you save per month: "))
    rate         = float(input("Rate: "))
    years        = int(input("Years until retirement: "))
    print("Future balance $%.2f" % calculateFutureBalance(savePerMonth, rate, years))

if __name__ == '__main__':
    main()
