#I worked on this myself.

def numVowelsInFile(fileName):
    """
        The function has variables for each vowel, with both the vowel in uppercase and
        lowercase. Each vowel has a count variable starting at 0. 'Try' is used to cover errors later.
        The function opens whatever file is used as the fileName parameter. The function loops through
        each line of the file and loops through each character in the line and checks if it is a vowel.
        If it is, the corresponding count goes up by 1. The function then prints each count. If a
        FileNotFoundError, NameError, or IOError occurs where the entered file name does not exist or
        is incorrect, the program prints 'Invalid file name'.
            """
    a = 'Aa'
    e = 'Ee'
    i = 'Ii'
    o = 'Oo'
    u = 'Uu'
    acount = 0
    ecount = 0
    icount = 0
    ocount = 0
    ucount = 0
    try:
        file = open(fileName, 'r')
        #variable = file.read() saves file as an enter string　
        #variable = variable.lower() converts string to all lowercase
        #variable.count('a') counts the number of 'a' in variable
        for line in file:
            for character in line:
                if character in a:
                    acount += 1
                if character in e:
                    ecount += 1
                if character in i:
                    icount += 1
                if character in o:
                    ocount += 1
                if character in u:
                    ucount += 1
        print(acount)
        print(ecount)
        print(icount)
        print(ocount)
        print(ucount)

    except (FileNotFoundError, NameError, IOError):
        print('Invalid file name')
    

def mergeFiles(file1,file2,newFile):
    '''
        'Try' is used to cover errors later. The function opens whatever files are
        used as the file1, file2, and newFile parameter. The parameters file1 and file2
        are assigned to the variables f1 and f2, respectfully. The newFile parameter is a
        new file assigned to the variable f3. For each line in files 1 and 2, the line is
        added to the new file. If a FileNotFoundError, NameError, or IOError occurs where the entered file name does not exist or
        is incorrect, the program prints 'One of the two files could not be found'.
        
            '''
    try:
        f1 = open(file1, 'r')
        f2 = open(file2, 'r')
        f3 = open(newFile, 'w')
        for line in f1:
            f3.write(line)
        for line in f2:
            f3.write(line)

    except (FileNotFoundError, NameError, IOError):
        print('One of the two files could not be found')


