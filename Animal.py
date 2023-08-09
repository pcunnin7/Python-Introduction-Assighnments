class Animal (object):
    def __init__(self, s = 'none', l = 'none'):
        self.species = s
        self.language= l
        self.sleeping = False
        print("I'm in memory")

    def sleep(self):
        self.sleeping = True

    def wakeup(self):
        self.sleeping = False
        
    def setSpecies(self,name):
        #a method is a function tied to an object
        self.species = name
    def getSpecies(self):
        return self.species
    def setLanguage(self, lang):
        self.language = lang
    def getLanguage(self):
        return self.language
    def speak(self):
        if self.sleeping == False:
            return ('I am a ' + self.species + ' and I ' + self.language)
        if self.sleeping == True:
            return('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
    def __str__(self):
        return '{}:{}'.format(self.species, self.language)
    def __repr__(self):
        return "Animal('{}','{}')".format(self.species, self.language)
    def __add__(self, other):
        len1 = len(self.getSpecies())
        len2 = len(other.getSpecies())
        an1 = self.getSpecies()[:-1]
        an2 = other.getSpecies()[1:]
        len3 = len(self.getLanguage())
        len4 = len(other.getLanguage())
        lan1 = self.getLanguage()[:-1]
        lan2 = other.getLanguage()[1:]
        return Animal(an1 + an2,lan1 + lan2)
    def __mul__(self,copies):
        clones = []
        for i in range(copies):
            clones.append(eval(repr(self)))
        return clones

class bird(Animal):
    def __init__(self, lang = 'chirp'):
        Animal.__init__(self, 'bird', lang)

    def __repr__(self):
        return "bird('{}')".format(self.language)
    def fly(self,n):
        if self.sleeping == False:
            print('I am flying {} feet'.format(n))
        if self.sleeping == True:
            print('I am sleeping')
    def __iter__(self):
        return iter(self.animals)

class Zoo(object):
    def __init__(self):
        self.animals = []

    def addAnimal(self,animal):
        self.animals.append(animal)
    def __iter__(self):
        return iter(self.animals)
    def speakAll(self):
        for animal in self.animals:
            print(animal.speak())
    def getAllSpecies(self):
        species = set()
        for animal in self.animals:
            species.add(animal.species)
        return species
    def __len__(self):
        return len(self.animals)
    def getItem(self,index):
        return self.animals[index]
    #def setItem(self,index,value):
        
            
'''
def saveAnimal(lst,filename):
    try:
        file = open(filename, 'w')
        for a in lst:
            file.write('{}\n'.format(str(a)))
        file.close()
        return True
    except:
        print('Unable to write files.')
        return False
        '''

def loadAnimal(filename):
    lst = []
    try:
        infile = open(filename, 'r')
        lines = infile.readlines()
        infile.close()
        for line in lines:
            parts = line.strip().split(':')
            lst.append(Animal(parts[0], parts[1]))
        return list
    except:
        print('Unable to read file')
            
    


class movie(object):
    def __init__(self, n, d, y , c, r):
        self.name = n
        self.director = d
        self.release = y
        self.country = c
        self.runtime = r
        self.list = [n, d, y, c, r]

    def getList(self):
        return self.list
    def getName(self):
        return self.name
    def getDirector(self):
        return self.director
    def getRelease(self):
        return self.release
    def getCountry(self):
        return self.country
    def getRuntime(self):
        return self.runtime
    def speak(self):
        return (str(self.getName()) + ' ' + str(self.getRelease()) + ' (' + str(self.getCountry()) + ') ' + '- Directed by ' + str(self.getDirector()) + ' (' + str(self.getRuntime()) +'minutes)')
    def __str__(self):
        return '{}:{}:{}:{}:{}'.format(self.name, self.director,self.release,self.country,self.runtime)

'''
def makeList():
    n1 = input('What is the name of your favorite movie? ')
    d1 = input('Who directed your favorite movie? ')
    y1 = input('What year did it come out? ')
    c1 = input('What country is it from? ')
    r1 = input('How long is it in minutes? ')
    m1 = movie(n1, d1, y1, c1, r1)
    rt = m1.getRuntime()
    rtn = float(rt)
    hours = int(rtn // 60)
    minutes = int(rtn % 60)
    print(m1.getName() + ' ' + m1.getRelease() + ' (' + m1.getCountry() + ') ' + '- Directed by ' + m1.getDirector() + ' (' +str(hours) + 'hr ' + str(minutes) + 'min)')

makeList()
    '''
