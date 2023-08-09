def extractStr(lst):
    if lst == []:
        return ''
    if type(lst[0]) == str:
        return lst[0] + extractStr(lst[1:])
    if type(lst[0]) == list:
        return extractStr(lst[0]) + extractStr(lst[1:])
    if type(lst[0]) != str:
        return extractStr(lst[1:])
    
lst=[1,2,[3,4,[5,6]],7,8,[[[[[[9]]]]]]]


def totalNumericValue(lst):
    if lst == []:
        return 0
    if type(lst[0]) == int or type(lst[0]) == float:
        return lst[0] + totalNumericValue(lst[1:])
    if type(lst[0]) == list:
        return totalNumericValue(lst[0]) + totalNumericValue(lst[1:])
    if type(lst[0]) != int and type(lst[0]) != float:
        return totalNumericValue(lst[1:])
