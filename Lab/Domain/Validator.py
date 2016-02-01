'''
Created on Nov 25, 2015

@author: Mada
'''
from Domain.Student import Student
from Domain.Problema import Problema
from Domain.Note import Note

'''
Se returneaza erorile de la un moment dat
'''
class ValidatorException(Exception):
    def __init__(self,errors):
        self.errors = errors

    def getMsgs(self):
        return self.errors
    
    def __str__(self):
        return str(self.errors)


class ValidatorStudent():
    def __init__(self,st):
        self.st = st
    '''
    st - tip 'class Student'
    '''
    def Validate_Student(self):
        errors = []
        
        '''
        Se verifica ca numele sa aiba cel putin un caracter 
        '''
        if self.st.Get_Stud_Name() == "":
            errors.append("Numele trebuie sa contina cel putin un caracter.")
           
        '''
        Se verifica ca numele sa fie compus doar din caractere litere
        '''
        if self.st.Get_Stud_Name().isalpha() == False:
            errors.append("Numele trebuie sa fie compus doar din caractere litere.")
        
        '''
        Se verifica ca grupul dat sa aiba caractere ( sa nu fie NULL )
        '''
        ok = 1
        if self.st.Get_Stud_Group() == "" :
            errors.append("Grupul studentului trebuie sa aiba cel putin un caracter.")
            ok = 0
            
        '''
        Se verifica ca grupul dat sa fie compus doar din cifre
        '''
        if ok == 1:
            try:
                m = int(self.st.Get_Stud_Group())
                if m < 1:
                    errors.append("Grupa studentului trebuie sa fie un numar natural mai mare ca 0.")
            except:
                errors.append("Grupa trebuie sa fie formata doar din caractere cifre.")
        
        '''
        Se vefifica ca ID-ul dat sa aiba cel putin un caracter ( sa nu fie NULL )
        '''
        ok = 1
        if self.st.Get_Stud_ID() == "":
            errors.append("Id-ul studentului trebuie sa aiba cel putin un caracter.")
            ok = 0
        
        '''
        Se verifica ca ID-ul dat sa fie compus doar din caractere cifre
        '''
        if ok == 1:
            try:
                m = int(self.st.Get_Stud_ID())
                if m < 1:
                    errors.append("ID-ul studentului trebuie sa fie un numar natural mai mare ca 0.")
            except:
                errors.append("ID-ul trebuie sa fie format doar din caractere cifre.")
        
        '''
        Daca exista erori dupa ce se verifica datele unui student, se afiseaza
        '''
        if len(errors) > 0:
            raise ValidatorException(errors)
        
        
class ValidatorProblema():
    def __init__(self,pb):
        self.pb = pb
    '''
    pb - tip 'class Problema'
    '''
    def Validate_Problem(self):
        errors = []
        
        '''
        Se verifica ca numarul laboratorului sa aiba cel putin un caracter si sa fie format doar din caractere cifre
        '''
        ok = 1
        if self.pb.Get_Nr_Lab() == "":
            errors.append("Numarul laboratorului trebuie sa aiba cel putin un caracter.")
            ok = 0
            
        if ok == 1:
            try:
                m = int(self.pb.Get_Nr_Lab())
                if m < 1:
                    errors.append("Numarul laboratorului trebuie sa fie un numar natural mai mare ca 0.")
            except:
                errors.append("Numarul laboratorului trebuie sa fie format doar din caractere cifre.")
                
        '''
        Se verifica ca numarul problemei sa aiba cel putin un caracter si sa fie format doar din caractere cifre
        '''
        ok = 1
        if self.pb.Get_Nr_Prob() == "":
            errors.append("Numarul laboratorului trebuie sa aiba cel putin un caracter.")
            ok = 0
            
        if ok == 1:
            try:
                m = int(self.pb.Get_Nr_Prob())
                if m < 1:
                    errors.append("Numarul problemei trebuie sa fie un numar natural mai mare ca 0.")
            except:
                errors.append("Numarul laboratorului trebuie sa fie format doar din caractere cifre.")
                
        '''
        Se verifica ca descrierea problemei sa aiba cel putin un caracter
        '''
        if self.pb.Get_Description() == "":
            errors.append("Descrierea problemei trebuie sa aiba cel putin un caracter.")
        
        '''
        Se verifica ca data sa fie specificata sub format zz/mm/yy
        '''
        prob = self.pb.Get_Deadline().split('/')

        '''
        In cazul in care nu este specificata in formatul cerut, se ridica clasa ValidatorException si se afiseaza erorile
        '''
        if len(prob) != 3:
            errors.append("Deadline-ul trebuie sa fie de tipul zz/mm/yy.")
            raise ValidatorException(errors)
        
        '''
        Se verifica ca datele sa fie formate doar din caractere cifre si sa corespunda conditiilor (zi: 1-31,luna: 1-12, an:2015 - )
        '''
        try:
            prob[0] = int(prob[0])
            prob[1] = int(prob[1])
            prob[2] = int(prob[2])
            if prob[0] < 1 or prob[0] > 31 or prob[1] < 1 or prob[1] > 12 or prob[2] < 2015:
                errors.append("Datele trebuie sa corespunda conditiilor: ziua: 1-31, luna: 1-12, anul: 2015 -  ")
        except:
            errors.append("Datele trebuie sa fie formate doar din caractere cifre.")
            
        if len(errors) > 0:
            print("raise")
            raise ValidatorException(errors)
        
    
class ValidatorNote():
    '''
    nott - tip 'class Note'
    '''
    def __init__(self,nott):
        self.nott = nott
    
    def Validate_Nota(self):
        errors = []
        
        '''
        Se verifica daca datele studentului au fost introduse corect.
        - nu ar trebui sa se ajunga aici
        '''
        ver_st = ValidatorStudent(self.nott.student)
        try:
            ver_st.Validate_Student()
        except ValidatorException as e:
            nr = e.__str__()
            if len(nr) > 0:
                errors.append("Studentul nu are datele introduse valide.")
        
        '''
        Se verifica daca datele problemei au fost introduse corect.
        - nu ar trebui sa se ajunga aici
        '''
        ver_pb = ValidatorProblema(self.nott.problem)
        try:
            ver_pb.Validate_Problem()
        except ValidatorException as e:
            nr = e.__str__()
            if len(nr) > 0:
                errors.append("Problema data nu are datele introduse valide.")
                
        '''
        Se verifica ca nota sa contina doar caractere cifre si sa fie cuprinsa intre 1 si 10
        '''
        ok = 1
        if self.nott.nota == "":
            errors.append("Nota introdusa trebuie sa aiba cel putin un caracter cifra.")
            ok = 0
        if ok == 1:
            try:
                a = int(self.nott.nota)
                if a < 1 or a > 10:
                    errors.append("Nota introdusa nu este valida. Introduceti o nota cuprinsa intre 1 si 10.")
            except:
                errors.append("Nota introdusa trebuie sa aiba doar caractere cifre.")
        
        '''
        Daca exista erori, se da raise ValidatorException
        '''
        if len(errors)>0:
            raise ValidatorException(errors)
        
        
def testValidatorStudent():
    st = Student("Mihai55", 20 ,11)
    ver = ValidatorStudent(st)
    try:
        ver.Validate_Student()
    except ValidatorException as e:
        assert e.__str__() == "['Numele trebuie sa fie compus doar din caractere litere.']"
    
    
def testValidatorProblema():
    pb = Problema(4,12,'primele 2 puncte','11/12/2015')
    ver = ValidatorProblema(pb)
    try:
        ver.Validate_Problem()
    except ValidatorException as e:
        assert e.__str__() == "[]"
        
def testValidatorNota():
    st = Student("Mihai4",4,11)
    pb = Problema(4,12,'primele 2 puncte','11/12/2015')
    
    '''
    SPN = Student Problem Note
    '''
    SPN = Note(st,pb,8)
    ver = ValidatorNote(SPN)
    try:
        ver.Validate_Nota()
    except ValidatorException as e:
        assert e.__str__() == "['Studentul nu are datele introduse valide.']"
        
testValidatorStudent()
testValidatorProblema()
testValidatorNota()



        
        
        
            
            

        
    
        
        

        
            
        
    
    

