

def swapCase(text):
    DIFFERENCE = ord('a') - ord("A")
    out = ""
    for character in text:
        if character >= "a" and character <= "z":
           out = out + chr(ord(character) - DIFFERENCE)
        elif character >= "A" and character <= "Z":
            out = out + chr(ord(character) + DIFFERENCE)
        else: 
            out = out + character

    return out


def count(text, match):
    x = 0
    for character in text:
        if character == match:
            x += 1
    return x

def onlyAlpha(within):
    cleaned = ""
    for x in within:
        if x.isalpha():
            cleaned += x
        
    '''
Takes out any non alphabetic characters (a-z, A-z) even spaces!
  within- the string to clean
 returns the cleaned string
    '''
    return cleaned

def reverse(text):
    reverse = ""
    for x in reversed(text):
        reverse += x
        
    
    
    '''
Swaps the order of all the characters in the string
   text - the string to reverse
 returns the reversed string
    '''
    return reverse

def markDoubles(within):
    y = ""
    marked = ""
    for x in within:
        if x == y:
            y = x
            x = "2" + x
        else:
            y = x
        marked += x
    '''
Annotate any repeated characters by placing a 2 between them
   within - the string to mark
 returns the marked string
    '''
    return marked

def isPalindrome(within):
    reverse = ""
    for x in reversed(within):
        reverse += x

    if reverse == within:
        palindrome = True
    else:
        palindrome = False
    '''
Check if the test is the same forward and back
   within - the string to check
 returns true if it is a palindrome
    '''
    return palindrome


#=================================================================
# Test code do not modify anything below here
def checkEquals(check, expected, testValue, message):
    '''
Check the test case adn report any errors
  check - the results of the test method
  expected - the expected value
  testValue - the input to the test case
  message - the error message to show if failed
 returns True if passed
    '''
    if check != expected:
        print(message, "your code returned", check, "and the test expected",
              expected, " for input string of", testValue)
        return False
    return True

def tester():
    totalStatus = True;

    testError = "onlyAlpha():"
    status = True
    status &= checkEquals(onlyAlpha("Tony Lowe"), "TonyLowe", "Tony Lowe", testError)
    status &= checkEquals(onlyAlpha("I’m excited!"), "Imexcited", "I’m excited!", testError)
    status &= checkEquals(onlyAlpha("&*(&#$*"), "", "&*(&#$*", testError)
    status &= checkEquals(onlyAlpha("2332 3443"), "", "2332 3443", testError)
    status &= checkEquals(onlyAlpha(""), "", "\"\"", testError)
    totalStatus = totalStatus and status
    print("onlyAlpha()" , "passed" if status else "failed")
         
    testError = "reverse() failed:";
    status = True
    status &= checkEquals(reverse("Tony Lowe"), "ewoL ynoT", "Tony Lowe", testError)
    status &= checkEquals(reverse("racecar"), "racecar", "racecar", testError)
    status &= checkEquals(reverse(""), "", "\"\"", testError)
    totalStatus = totalStatus and status
    print("reverse()", "passed" if status else "failed")   

    testError = "count(char) failed:"
    status = True
    status &= checkEquals(count("Tony Lowe", 'o'), 2, "\"Tony Lowe\", 'o'", testError)
    status &= checkEquals(count("Tony Lowe", ' '), 1, "\"Tony Lowe\", ' '", testError)
    status &= checkEquals(count("Tony Lowe", 'z'), 0, "\"Tony Lowe\", 'z'", testError)
    status &= checkEquals(count("racecar", 'r'), 2, "\"racecar\", 'r'", testError)
    status &= checkEquals(count("", ' '), 0, "\"\", ' '", testError)
    totalStatus = totalStatus and status
    print("count(char)", "passed" if status else "failed");        

    testError = "swapCase() failed:"
    status = True
    status &= checkEquals(swapCase("Tony Lowe"), "tONY lOWE", "\"Tony Lowe\"", testError)
    status &= checkEquals(swapCase("!@#$%"), "!@#$%", "\"!@#$%\"", testError)
    status &= checkEquals(swapCase("aaaa"), "AAAA", "\"aaaa\"", testError)
    status &= checkEquals(swapCase(""), "", "\"\", \" \"", testError)
    totalStatus = totalStatus and status
    print("swapCase()", "passed" if status else "failed")

    testError = "markDoubles()"
    status = True
    status &= checkEquals(markDoubles("Mississippi"), "Mis2sis2sip2pi", "\"Mississippi\"", testError)
    status &= checkEquals(markDoubles("aaaa"), "a2a2a2a", "\"aaaa\"", testError)
    status &= checkEquals(markDoubles(""), "", "\"\", \" \"", testError)
    totalStatus = totalStatus and status
    print("markDoubles()", "passed" if status else "failed")

    testError = "isPalindrome()"
    status = True
    status &= checkEquals(isPalindrome("racecar"), True, "\"racecar\"", testError)
    status &= checkEquals(isPalindrome("Madam"), False, "\"Madam\"", testError)
    status &= checkEquals(isPalindrome("aaaa"), True, "\"aaaa\"", testError)
    status &= checkEquals(isPalindrome(""), True, "\"\", \" \"", testError)
    totalStatus = totalStatus and status
    print("isPalindrome()", "passed" if status else "failed")
    return totalStatus

if __name__ == '__main__':
    if tester():
        print ("All Tests Passed!")
