#I worked on this alone
from tkinter import Button, Label,Tk,Text,INSERT,TOP,LEFT,RIGHT,END,filedialog, Scale, HORIZONTAL
from tkinter.messagebox import showinfo

#Put problem 1 here.

class textEditor(Tk):
    def __init__(self,parent = None):
        Tk.__init__(self,parent)
        self.title('Text')
        self.make_widgets()
        self.f = ''

    def open(self):
        self.text.delete(1.0,END)
        file=open(filedialog.askopenfilename())
        f = file.read()
        self.text.insert(INSERT, f)
        file.close()
        
    def save(self):
        txt = self.text.get(1.0,END)
        file=open(filedialog.askopenfilename(), 'w')
        file.write(txt)
        
        
    
    def make_widgets(self):
        Label(self, text="File Name:").grid(row = 0, column = 0)
        
        self.text = Text(self, width = 20, height = 5, highlightthickness=2)
        self.text.grid(row = 0, column = 1)

        Button(self, text="Open", command=self.open).grid(row = 0, column = 2)
        Button(self, text="Save", command=self.save).grid(row = 0, column = 3)
        

def stringWithVowelCount(lst):
    if lst == []:
        return 0
    if type(lst[0]) == str:
        if 'a' in lst[0] or 'A' in lst[0] or 'e' in lst[0] or 'E' in lst[0] or 'I' in lst[0] or 'i' in lst[0] or 'O' in lst[0] or 'o' in lst[0] or 'u' in lst[0] or 'U' in lst[0]:
            return 1 + stringWithVowelCount(lst[1:])
        else:
            return 0 + stringWithVowelCount(lst[1:])
    if type(lst[0]) == list:
        return stringWithVowelCount(lst[0]) + stringWithVowelCount(lst[1:])
    if type(lst[0]) != str:
        return stringWithVowelCount(lst[1:])

print(stringWithVowelCount([]))                               
print(stringWithVowelCount([[1,'Test',2.0,'v','other',1,2,'bbbbb',8,9,10]]))
print(stringWithVowelCount([[[[[[[[['nnnnnnnnn']]]]]]]]]))
print(stringWithVowelCount([[1,'Anthony',2,3],[4,[[[5,[[[6,'Bob']]]]]]]]))
print(stringWithVowelCount([[[[[[[[[10,20],'Carl']]]]]]]]))
print(stringWithVowelCount([[[[[[[[[]]]]]]]]]))

    
import os

def dirPrint(pathname, indent):
    '''recursively scans all files contained, directly or
       indirectly, in the folder pathname'''
    print(' ' * indent + pathname)
    for item in os.listdir(pathname):
        n = os.path.join(pathname, item)
        if os.path.isdir(n):
            #FOLDER
            dirPrint(n, indent +1)
        
        
dirPrint('count',4)
dirPrint('Test',6)



def frequency(pathname, word,count):
    lst = []
    for item in os.listdir(pathname):
        sublist = []
        n = os.path.join(pathname, item)
        if os.path.isdir(n):
            #FOLDER
            sublist.extend(frequency(n, word,count))
        else:
            infile = open(n, 'r')
            f = infile.read()
            x = f.count(word)
            if x >= count:
                infile.close()
                sublist.append(n)
            else:
                infile.close()
        lst.extend(sublist)
    return lst

print('FREQUENCY: \n', frequency('Test','assign',1))
print('FREQUENCY: \n', frequency('Test-2','e',2))
print('FREQUENCY: \n', frequency('Test','e',2))
print('FREQUENCY: \n', frequency('Test-2','Zoko',1))
print('FREQUENCY: \n', frequency('Test','Y',1))
print('FREQUENCY: \n', frequency('Test','Y',2))



def directoryFileSize(folder):
    'return the length of all the files in the directory and subdirectories'
    count = 0
    for item in os.listdir(folder):
        n = os.path.join(folder, item)
        if os.path.isdir(n):
            #FOLDER
            count += directoryFileSize(n)
        else:
            infile = open(n, 'r')
            f = infile.read()
            count += (len(f))
    return (count)

print(directoryFileSize('Test'))
print(directoryFileSize('Test-2'))







