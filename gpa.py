def calculateFutureBalance (amountPerMonth, annualRate, yearsSaved):
        total = 0
        for month in range (yearsSaved * 12):
                print(total, total * annualRate/12)
                total = total + amountPerMonth
                total = total + total * annualRate/12

        return total

def main ():
        savePerMonth = int(input("How much will you save "))
        rate = float(input("Rate: ")) /100
        years = int(input("Years until retirement "))
        print("Fututre balance $%.2f" % calculateFutureBalance(savePerMonth, rate, years))


if __name__ == '__main__':
        main()
                    
