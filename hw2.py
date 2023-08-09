#I worked on this alone
#Question 1:

class Engine(object):
    '''
    A class that represents an engine
'''
    def __init__(self):
        '''
    A method that constructs an engine and assigns values to speed and on
'''
        self.speed = 0
        self.on = False

    def powerOn(self):
        'turn on the engine, or get the message Engine is already on if it is'
        if self.on == False:
            self.on = True
            return('Engine is on')
        if self.on == True:
            return('Engine is already on')
        

    def powerOff(self):
        'turn off the engine, or get the message Engine is already off if it is'
        if self.on == True:
            self.on = False
            return('Engine is off')
        if self.on == False:
            return('Engine is already off')
        

    def increaseSpeed(self,amount):
        'increase the speed if adding amount to the speed keeps the speed under 100'
        if self.on == True:
            if self.speed + amount <= 100:
                self.speed += amount
            elif self.speed + amount > 100:
                return('Cannot exceed 100 rpm')
            
            

    def decreaseSpeed(self,amount):
        'decrease the speed if subtracting amount from the speed keeps the speed over 0'
        if self.on == True:
            if self.speed - amount >= 0:
                self.speed = self.speed - amount
            elif self.speed - amount < 0:
                return("Can't decrease speed to less than 0 rpm.")
                
    def __str__(self):
        'string operator'
        if self.on == True:
            if self.speed == 0:
                status = 'on but idle'
            if self.speed > 0:
                status = 'on and running at {} rpm'.format(self.speed)
        if self.on == False:
            status = 'off'
        return ('Engine is {}'.format(status))

#Question 2:
    
class Teacher(object):
    'a class that represents an Teacher'
    
    def __init__(self,name,email,phone):
        'Teacher constructor'
        self.reqname = name
        self.reqemail = email
        self.reqphone = phone
        

    def getName(self):
        'get the teacher name'
        return self.reqname

    def setName(self,name):
        'set the teacher name'
        self.reqname = name

    def getPhone(self):
        'get phone location'
        return self.reqphone

    def setPhone(self,phone):
        'set phone location'
        self.reqphone = phone

    def getEmail(self):
        'get email address'
        return self.reqemail

    def setEmail(self,email):
        'set email address'
        self.reqemail = email

    def __str__(self):
        'string operator'
        return('Teacher {} email address is {}. Their phone number is {}.'.format(self.reqname, self.reqemail,self.reqphone))
    

        
    def __repr__(self):
        'repr operator'
        return("Teacher('{}', '{}', '{}')".format(self.reqname, self.reqemail,self.reqphone))
    
#QUESTION 3
#This class definition had not been provided.  You must write it yourself.

class Professor(Teacher):
    def __init__(self,name,email,phone, researchArea):
        'Constructs professor with additional value of researchArea'
        Teacher.__init__(self,name,email,phone)
        self.area = researchArea

    def getResearchArea(self):
        'get researchArea'
        return self.area
    def setResearchArea(self, researchArea):
        'set researchedArea'
        self.area = researchArea
    def __str__(self):
        'string operator'
        return('Professor {} email address is {}. Their phone number is {}. Their research area is {}.'.format(self.reqname, self.reqemail,self.reqphone, self.area))
    

        
    def __repr__(self):
        'repr operator'
        return("Professor('{}', '{}', '{}', '{}')".format(self.reqname, self.reqemail,self.reqphone, self.area))

    
    

#QUESTION 4:
#Initializing types from file data

def loadTeachers(filename):
    'load teachers, based on type from file'
    try:
        List = []
        infile = open(filename, 'r')
        lines = infile.readlines()
        infile.close()
        for line in lines:
            entries = line.strip().split("'\n'")
            for entry in entries:
                parts = entry.strip().split(',')
                if parts[-1] != '':
                    List.append(Professor(parts[0],parts[1],parts[2],parts[3]))
                elif parts[-1] == '':
                    List.append(Teacher(parts[0],parts[1],parts[2]))
                    
                
        return List
    except:
        print('Unable to read file')
    

for s in loadTeachers('teachers.txt'):
        print(s)

