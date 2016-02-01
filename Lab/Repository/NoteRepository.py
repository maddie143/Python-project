'''
Created on Nov 26, 2015

@author: Mada
'''
from Domain import Note
from Domain import Student
from Repository.StudentRepository import StudentRepository


class RepositoryExceptionNote(Exception):
    def __str__(self):
        return "Datele introduse nu exista."
    
class RepositoryExceptionNoteE(Exception):
    def __str__(self):
        return "Datele introduse exista deja."
    
class NoteRepository:
    '''
    Se folosesc repository-urile ProblemRepository si StudentRepository
    '''
    def __init__(self):
        self.note = {}
        
    '''
    Se adauga o nota noua - student: 'class Student' , problema: 'class Problema'
    '''
    def Add_Nota(self, student, problema, nota):
        new_nota = Note.Note(student,problema, nota)
        m        = len(self.note)
        for i in range(0,m):
            if self.note[i].Get_Prob() == problema and self.note[i].Get_Stud() == student.Get_Stud_Name():
                raise RepositoryExceptionNote
            
        self.note[len(self.note)] = new_nota

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
        return li
    
    
def Test_Add_Note():
    rep1    = StudentRepository()
    rep2    = NoteRepository()
    student = Student.Student('Ion','211',len(rep1.students))
    rep2.Add_Nota(student, '4.3',8)
    rep2.Add_Nota(student, '4.2',9)
    
    assert rep2.Get_Nr_Of_Notes() == 2
    
Test_Add_Note()

   
        
        
    
            
        