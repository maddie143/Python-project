'''
Created on Nov 25, 2015

@author: Mada
'''
from Domain.Validator import ValidatorNote
from Repository.StudentRepository import StudentRepository
from Domain import Note,Student,Problema
from Repository.ProblemRepository import ProblemRepository
from Repository.NoteRepository import NoteRepository

class NoteController:
    def __init__(self, NoteRep, StudRep):
        self.NoteRep = NoteRep
        self.StudRep = StudRep
        
    """
    Se atribuie o nota elevului cu numele 'nume' la problema 'problema
    """
    def AddNota(self, nume, problema, nota):
        st   = self.StudRep.Find_By_Name(nume)
        nott = Note.Note(nume,problema,nota)
        ValidatorNote(nott)
        self.NoteRep.Add_Nota(st, problema, nota)
        
    """
    Se returneaza lista cu notele
    """
    def GetNote(self):
        return self.NoteRep.Get_List_Of_Notes()
    
    """
    Se returneaza lista notelor unei probleme
    """
    def GetProbsStud(self,prob):
        return self.NoteRep.Get_Problem_Grades(prob)
    
    
    
def TestAddNote():
    
    rep     = StudentRepository()
    rep1    = ProblemRepository()
    rep2    = NoteRepository()
    ctr     = NoteController(rep2,rep)
    
    student = Student.Student('Ion','213',len(rep.students))
    rep.Save_Student(student)
    assert rep.Nr_Students() == 1
    prob = Problema.Problema(4,3,'aaa','5/5/2009')
    rep1.Save_Problem(prob)
    ctr.AddNota('Ion', '4.3', 8)
    notele = ctr.GetNote()
    assert len(notele)== 1

TestAddNote()
        
        