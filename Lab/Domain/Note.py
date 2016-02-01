'''
Created on Nov 25, 2015

@author: Mada
'''
from Domain.Student import Student
from Domain.Problema import Problema

class Note():
    def __init__(self,student,problem,nota):
        self.student = student
        self.problem = problem
        self.nota    = nota
        
    '''
    Se returneaza nota pentru problema curenta
    '''
    def Get_Nota(self):
        an = self.nota
        return an
    
    '''
    Se seteaza/actualizeaza nota pentru problema curenta
    '''
    def Set_Nota(self,new_nota):
        self.nota = new_nota
    
    '''
    Se returneaza numele studentului
    '''
    def Get_Stud(self):
        #print(self.student)
        return self.student #tip Student
    
    
    '''
    Se returneaza problemas
    '''
    def Get_Prob(self):
        return self.problem
    
    '''
    Se afiseaza datele studentului cu problema si nota primita
    '''
    def Show_Nota(self):
        print("Studentul " + str(self.student.Get_Stud_Name()) + " a primit nota " + str(self.nota.Get_Nota())+ " pe problema " + str(self.Get_Problem())+".")
        print()
        
        
def testNote():
    St  = Student("Andrei",12,1)
    Pb  = Problema(7,13,"primele 2 puncte","11/11/2015")
    Not = Note(St,Pb,5)
    assert Not.Get_Nota() == 5
    #sassert Not.Get_Stud() == "Andrei"
    assert Not.Get_Prob().Get_Nr_Prob() == 13
    
testNote()
    