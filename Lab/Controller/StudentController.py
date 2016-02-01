'''
Created on Nov 25, 2015

@author: Mada
'''

from Domain import Student
from Repository import StudentRepository
from Domain.Validator import ValidatorStudent



class StudentController:
    def __init__(self,repository):
        self.repository = repository
        
    """
    Se adauga un nou student.
    Se verifica ca datele sa indeplineasca conditiile si ca elevul sa nu mai exista in 
    repository.
    """
    def AddStudent(self,nume,grupa):
        #Se seteaza un nou student
        Id = self.repository.Nr_Students() + 1
        new_st = Student.Student(nume,grupa,Id)
        
        #Se valideaza datele studentului
        ValidatorStudent(new_st)
        
        #Se salveaza in repository
        self.repository.Save_Student(new_st)
        

            
    '''
    Sterge student dupa ID
    '''
    def DeleteStudent(self,ID):
        self.repository.Delete_By_ID(ID)
        
    '''
    Se actualizeaza datele unui student
    Se verifica ca noile date sa indeplineasca conditiile, iar in caz afirmativ, se salveaza
    '''
    def UpdateStudent(self,nume,grupa,ID):
        new_stud = Student.Student(nume,grupa,ID)
        
        ValidatorStudent(new_stud)
        self.repository.Update_Student(nume,grupa,ID)
    
    '''
    Se cauta un elev dupa ID
    '''
    def FindStudentByID(self,ID):
        return self.repository.Find_By_ID(ID)
    
    '''
    Se cauta un student dupa nume
    '''
    def FindStudentByName(self,nume):
        return self.repository.Find_By_Name(nume)
    
    '''
    Se returneaza toti studentii apeland direct students
    '''
    def GetStudents1(self):
        return(self.repository.students)
    
    '''
    Se returneaza toti studentii apeland repository-ul
    '''
    def GetStudents(self):
        return(self.repository.Get_Students())
    
    
    def ret_st_name(self,name):
        for i in self.repository.students:
            if self.repository.students[i].Get_Stud_Name() == name:
                return self.repository.students[i]
        return 0
        
def testAddStudent():
    
    rep = StudentRepository.StudentRepository()
    st = Student.Student('mihai','213',len(rep.students))
    ctr = StudentController(rep)
    ctr.AddStudent('mihai', '213')
    assert st.Get_Stud_ID() == 0
    assert st.Get_Stud_Name() == 'mihai'
    
    
    allsts = ctr.GetStudents()
    assert len(allsts) == 1
    assert allsts[0].Get_Stud_Name() == st.Get_Stud_Name()
    
    st = Student.Student('Go','211',len(rep.students))
    ctr.AddStudent('Go', '211')
    allsts = ctr.GetStudents()
    assert st.Get_Stud_ID() == 1
    assert allsts[1].Get_Stud_Name() == 'Go'
    
    allsts = ctr.GetStudents()
    assert len(allsts) == 2
    assert allsts[1].Get_Stud_Group() == st.Get_Stud_Group()

testAddStudent()