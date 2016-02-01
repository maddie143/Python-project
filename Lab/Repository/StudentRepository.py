'''
Created on Nov 26, 2015

@author: Mada
'''
from Domain.Student import Student

class RepositoryExceptionStud(Exception):
    def __str__(self):
        return "Nu exista studentul cu aceste date in repository."

class StudentRepository:
    def __init__(self):
        self.students = {}
        
    '''
    Se seteaza id-ul noului student cu lungimea array-ului de studenti
    '''
    def Save_Student(self,student):
        student.Set_ID(len(self.students))
        for i in self.students:
            if self.students[i] == student:
                raise RepositoryExceptionStud()
            
        self.students[len(self.students)] = student

        
    """
    Se cauta un student dupa ID, in cazul in care exista se returneaza studentul,
    altfel se ridica eroare ValueError
    """
    def Find_By_ID(self,ID):
        if ID <= len(self.students):
            return self.students[ID]
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
            if int(c[i].Get_Stud_ID()) == int(ID) and ok == 0:
                self.students[i].Set_Name(nume)
                self.students[i].Set_Group(grupa)
                ok = 1
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
    def Get_Stud(self,student):
        return self.student
    
            
def TestSaveStudent():
    '''
    Se testeaza daca se adauga in rep
    '''
    rep     = StudentRepository()
    student = Student('Ion','213',len(rep.students))
    
    # = 0 pentru ca nu a fost salvat
    assert len(rep.students) == 0
    
    rep.Save_Student(student)
    #a fost salvar, deci rep.size() creste
    assert len(rep.students) == 1
    
    student1 = Student('Mircea','211',len(rep.students))
    rep.Save_Student(student1)
    assert len(rep.students) == 2
    

def TestUpdate():
    rep     = StudentRepository()
    student = Student('Ion','213',len(rep.students))
    
    rep.Save_Student(student)
    # Se salveaza studentul
    rep.Update_Student('Mihai', '10', int(student.Get_Stud_ID()))
    #Se updateaza
    
    allsts = rep.Get_Students()
    # Se testeaza sa existe datele corespunzatoare
    assert allsts[0].Get_Stud_Name() == 'Mihai'
    assert allsts[0].Get_Stud_Group() =='10'

TestSaveStudent()
TestUpdate()
