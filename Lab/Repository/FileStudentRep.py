'''
Created on Dec 15, 2015

@author: Tincarica
'''

from Domain.Student import Student
class RepositoryExceptionStud(Exception):
    def __str__(self):
        return "Nu exista studentul cu aceste date in repository."

class RepositoryFileException(Exception):
    def __init__(self,error):
        self.error = error
    def __str__(self):
        return("Studentul exista deja in repository.")

class FileStudentRep:
    def __init__(self,fileName):
        self.fileName = fileName
        self.students = {}
        self.loadFromFile()
        
        
    """
    Se incarca datele din fisier in memorie.
    """
    def loadFromFile(self):
        try:
            f = open(self.fileName,"r")
        except IOError:
            return []
        
        line = f.readline().strip()
        while line!= "":
            attrs = line.split(" ")
            st    = Student(attrs[0], attrs[1], attrs[2])
            self.students[len(self.students)] = st
            line  = f.readline().strip()
        f.close()
        #return self.students

    """
    Se salveaza datele din memorie in fisier.
    """
    def storeToFile(self):
        f = open(self.fileName,"w")
        for st in self.students:
            #print(st,type(st))
            strf = str(self.students[st].Get_Stud_Name()) + " " + str(self.students[st].Get_Stud_Group()) + " " + str(self.students[st].Get_Stud_ID() )
            strf = strf + "\n"
            f.write(strf)
        f.close()
        

    def store(self,st):
        allStudents = self.students
        #print(type(allStudents))
        if st in allStudents:
            raise RepositoryFileException
        #self.students[len(self.students)] = st
        self.storeToFile()
        
    
    '''
    Se seteaza id-ul noului student cu lungimea array-ului de studenti
    '''
    def Save_Student(self,student):
        student.Set_ID(len(self.students))
        for i in self.students:
            if self.students[i] == student:
                raise RepositoryExceptionStud()
            
        
        self.students[len(self.students)] = student
        self.storeToFile()
        
        
    """
    Se cauta un student dupa ID, in cazul in care exista se returneaza studentul,
    altfel se ridica eroare ValueError
    """
    def Find_By_ID(self,ID):
        if ID <= len(self.students):
            for st in self.students:
                if self.students[st].Get_Stud_ID() == ID :
                    return self.students[st]
        else:
            raise RepositoryExceptionStud()

    """
    Se cauta un student dupa nume
    """
    def Find_By_Name(self,name):
        for i in self.students:
            if self.students[i].nume == name:
                return self.students[i]
            
        raise RepositoryExceptionStud
        
    """
    Se sterge un student dupa ID
    """
    def Delete_By_ID(self,ID):
        ok = 0
        for st in range(0,len(self.students)):
            if int(self.students[st].Get_Stud_ID()) == int(ID):
                self.students.pop(st)
                self.storeToFile()
                ok = 1
    
        if ok == 0:
            raise RepositoryExceptionStud
        
    """
    Se cauta ID-ul studentului in repository, daca exista, se modifica numele si grupa, daca
    nu exista, se ridica eroarea RepositoryException()
    """
    def Update_Student(self,nume,grupa,ID):
        c = self.students
        ok = 0
        for i in range(0,len(c)):
            #print(int(c[i].Get_Stud_ID()) == int(ID))
            if int(c[i].Get_Stud_ID()) == int(ID) and ok == 0:
                self.students[i].Set_Name(nume)
                self.students[i].Set_Group(grupa)
                ok = 1
                #print(c[i].Get_Stud_ID(), c[i].Get_Stud_Name())
                self.storeToFile()
        if ok == 0:
            raise RepositoryExceptionStud()
    
    """
    Se returneaza numarul total de studenti.
    """
    def Nr_Students(self):
        return len(self.students)
    
    """
    Se returneaza lista cu toti studentii.
    """
    def Get_Students(self):
        return list(self.students.values())

    """
    Se returneaza un student
    """
    def Get_Stud(self,idd):
        for i in self.students:
            if int(self.students[i].Get_Stud_ID()) == int(idd):
                return self.students[i]
        return 0
    
        
    