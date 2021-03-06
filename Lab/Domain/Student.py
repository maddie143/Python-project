'''
Created on Nov 25, 2015

@author: Mada
'''

class Student():
    def __init__(self,nume,grupa,ID):
        self.nume  = nume
        self.grupa = grupa
        self.ID    = ID
    
    '''
    Returneaza numele studentului
    '''
    def Get_Stud_Name(self):
        return self.nume
    
    '''
    Returneaza grupa studentului
    '''
    def Get_Stud_Group(self):
        return self.grupa
    
    ''' 
    Returneaza ID-ul studentului
    '''
    def Get_Stud_ID(self):
        return self.ID
    
    '''
    Se actualizeaza numele studentului
    '''
    def Set_Name(self,new_nume):
        self.nume = new_nume
        
    '''
    Se actualizeaza grupa studentului
    '''
    def Set_Group(self,new_grupa):
        self.grupa = new_grupa
        
    '''
    Se actualizeaza ID-ul studentului
    '''
    def Set_ID(self,new_ID):
        self.ID = new_ID
        
    '''
    Se verifica daca exista deja un student cu numele sau ID-ul
    respectiv
    Input:
        comp_name - obiect tip Student
    '''
    def Check_Existance(self,comp):
        return self.nume == comp.get_stud_nume() and self.ID == comp.get_stud_ID()
    
    '''
    Se afiseaza studentul cu toate datele sale
    '''
    def Show_Stud(self):
        print("Stundentul "+str(self.nume)+" din grupa "+str(self.grupa)+" are ID-ul "+str(self.ID)+".\n")
        print()
    
    
    
    
def testStudent():
    Stud = Student("Andrei",43,1)
    assert Stud.Get_Stud_Name() == "Andrei"
    assert Stud.Get_Stud_ID() == 1
    assert Stud.Get_Stud_Group() == 43
    Stud.Set_ID(55)
    assert Stud.Get_Stud_ID() == 55
    
    Stud1 = Student("Maria",11,2)
    assert Stud1.Get_Stud_Name() == "Maria"
    assert Stud1.Get_Stud_ID() == 2
    assert Stud1.Get_Stud_Group() == 11
    Stud1.Set_Name("Pavel")
    assert Stud1.Get_Stud_Name() == "Pavel"

testStudent()