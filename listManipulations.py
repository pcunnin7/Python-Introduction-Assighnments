
def total(values):
    z = 0
    for x in values:
        z += x
        
    '''
Add up all the numbers in the list
   values - a list of numbers
 returns the total
    '''
    return z

def mean(values):
    total = 0
    count = 0
    for x in values:
        total += x
        count += 1
    '''
Compute the mean of the values in the list
   values - a list of numbers
 returns the mean  
    '''
    if count == 0:
        mean = 0
    else:
        mean = (total / count)
    return mean

def count(values, find):
    count = 0
    for x in values:
        if find == x:
            count += 1
    return count

def median(values):
    z = 0
    values.sort()
    if len(values) > 0:
        if (len(values) % 2) == 0:
            w = ((len(values) / 2) - 1)
            x = int(w)
            z = ((values[x] + values[x+1]) / 2)
        else:
            y = ((len(values) / 2) - 1)
            v = y + .5
            u = int(v)
            z = values[u]            
    
    
    # The median is the 'middle value' of the list
    # If the list is odd, it is that value directly
    # If the list is even, it is the average of the middle two values
    # Hint: to sort your list, use the line
    # values.sort()    
    return z

def largest(values):
    if len(values) > 0:
        values.sort()
        y = len(values) -1 
        x = values[y]
    else:
        x = 0
    '''
Find the largest value in the list
  values - a list of numbers
    '''
    return x

def smallest(values):
    if len(values) > 0:
        values.sort()
        x = values[0]
    else:
        x = 0
    '''
Find the smallest value in the list
  values - a list of numbers
    '''
    return x

def tenTimes(values):
    if len(values) > 0:
        values.sort()
        y = values[0]
        for x in values:
            if x != 0:
                if x >= (10 * y):
                    ten = True
                else:
                    ten = False
            y = x
    else:
        ten = False
            
    '''
See if any value in this list is 10 times greater than another value
in the list, but watch out for 0!
  values - a list of numbers
    '''
    # Hint: The wrong logic will make any value look 10 times zero
    return ten

#=======================================================================
# Do not edit anything below here
def checkEquals(check, expected, inputList, message):
    if check != expected:
        print(message, "your code returned ", check, " but should have returned", expected, "for input", inputList)
        return False
    return True

def tester():
    totalStatus = True;
    basic = [2, 5, 10, 15]
    negative = [0, -5, -10]
    mixed = [-5, -1, 0, 1, 5]
    empty = []
            
    testError = "total() failed:"
    status = True
    status &= checkEquals(total(basic), 32, basic, testError)
    status &= checkEquals(total(negative), -15, negative, testError)
    status &= checkEquals(total(mixed), 0, mixed, testError)
    status &= checkEquals(total(empty), 0, empty, testError)
    totalStatus = totalStatus and status
    print("total() ", "passed" if status else "failed")

    testError = "mean()"
    status = True
    status &= checkEquals(mean(basic), 8.0, basic, testError)
    status &= checkEquals(mean(negative), -5.0, negative, testError)
    status &= checkEquals(mean(mixed), 0.0, mixed, testError)
    status &= checkEquals(mean(empty), 0.0, empty, testError)
    totalStatus = totalStatus and status
    print("mean() ", "passed" if status else "failed")

    testError = "count()"
    status = True
    multiple = [0, 5, 2, 3, 5, 2, -5, 5]
    status &= checkEquals(count(basic, 10), 1, basic, testError)
    status &= checkEquals(count(negative, 7), 0, multiple, testError)
    status &= checkEquals(count(multiple, 5), 3, multiple, testError)
    status &= checkEquals(count(empty, 0), 0, empty, testError)
    totalStatus = totalStatus and status
    print("count()", "passed" if status else "failed")

    testError = "median() failed: ";
    status = True
    status &= checkEquals(median(basic), 7.5, basic, testError)
    status &= checkEquals(median(negative), -5.0, negative, testError)
    status &= checkEquals(median(multiple), 2.5, multiple, testError)
    status &= checkEquals(median(mixed), 0.0, mixed, testError)
    status &= checkEquals(median(empty), 0.0, empty, testError)
    totalStatus = totalStatus and status
    print("median()", "passed" if status else "failed")

    testError = "largest()"
    status = True
    status &= checkEquals(largest(basic), 15, basic, testError)
    status &= checkEquals(largest(negative), 0, negative, testError)
    status &= checkEquals(largest(multiple), 5, multiple, testError)
    status &= checkEquals(largest(mixed), 5, mixed, testError)
    status &= checkEquals(largest(empty), 0, empty, testError)
    totalStatus = totalStatus and status
    print("largest()", "passed" if status else "failed")

    testError = "smallest()"
    status = True
    status &= checkEquals(smallest(basic), 2, basic, testError)
    status &= checkEquals(smallest(negative), -10, negative, testError)
    status &= checkEquals(smallest(multiple), -5, multiple, testError)
    status &= checkEquals(smallest(mixed), -5, mixed, testError)
    status &= checkEquals(smallest(empty), 0, empty, testError)
    totalStatus = totalStatus and status
    print("smallest()", "passed" if status else "failed")

    testError = "tenTimes()"
    status = True
    positive    = [1, 10, 100]
    negativeTen = [-1, -10, -100]
    status &= checkEquals(tenTimes(positive), True, positive, testError)
    status &= checkEquals(tenTimes(negativeTen), True, negativeTen, testError)
    status &= checkEquals(tenTimes(multiple), False, negative, testError)
    status &= checkEquals(tenTimes(mixed), False, mixed, testError)
    status &= checkEquals(tenTimes(empty), False, empty, testError)
    totalStatus = totalStatus and status
    print("tenTimes()", "passed" if status else "failed")

    return totalStatus

if __name__ == '__main__':
    if tester():
        print ("All Tests Passed!")
