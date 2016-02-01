'''
Created on Jan 12, 2016

@author: Tincarica
'''
from Domain.Note import Note

class FileException(Exception):
    def __str__(self):
        print("Studentul cu problema data apare deja.")

class FileNoteRep:
    def __init__(self,fileName,repStud):
        self.fileName = fileName
        self.repStud  = repStud
        self.note = {}
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
            if len(attrs) != 3:
                line  = f.readline().strip()
                continue
            
            #print(type(self.repStud))
            std   = self.repStud.Get_Stud(attrs[0])
            nt    = Note(std, attrs[1], attrs[2]) #Student,Problema,Nota
            
            self.note[len(self.note)] = nt
            line  = f.readline().strip()
        f.close()
        #return self.students

    """
    Se salveaza datele din memorie in fisier.
    """
    def storeToFile(self):
        f = open(self.fileName,"w")
        for st in self.note:
            strf = str(self.note[st].Get_Stud().Get_Stud_ID()) + " " + str(self.note[st].Get_Prob()) + " " + str(self.note[st].Get_Nota())
            strf = strf + "\n"
            f.write(strf)
        f.close()
        

    def store(self,st):
        allStudents = self.note
        #print(type(allStudents))
        if st in allStudents:
            raise FileException
        #self.students[len(self.students)] = st
        self.storeToFile()
        
    
    '''
    Se adauga o nota noua - student: 'class Student' , problema: 'class Problema'
    '''
    def Add_Nota(self, student, problema, nota):
        new_nota = Note(student,problema, nota)
        m        = len(self.note)
        for i in range(0,m):
            if self.note[i].Get_Prob() == problema and self.note[i].Get_Stud() == student.Get_Stud_Name():
                raise FileException
            

        self.note[len(self.note)] = new_nota
        self.storeToFile()


    '''
    Se returneaza numarul total de note
    '''
    def Get_Nr_Of_Notes(self):
        return len(self.note)
    
    '''
    Se returneaza o lista cu toate notele
    '''
    def Get_List_Of_Notes(self):
        return list(self.note.values())
    
    '''
    Pentru o problema data, se returneaza toate notele
    '''
    def Get_Problem_Grades(self, problem):
        li = []
        p  = len(self.note)
        for i in range(0,p):
            if int(self.note[i].Get_Prob()) == int(problem):
                li.append(self.note[i].Get_Stud().Get_Stud_Name())
                self.storeToFile()
        return li
    

        
    