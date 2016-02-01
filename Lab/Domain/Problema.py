'''
Created on Nov 25, 2015

@author: Mada
'''

class Problema():
    def __init__(self, nr_lab, nr_prob,descriere,deadline):
        self.nr_lab     = nr_lab
        self.nr_prob    = nr_prob
        self.descriere  = descriere
        self.deadline   = deadline

    '''
    Se returneaza o problema dupa numarul acesteia
    '''
    def Get_Nr_Prob(self):
        return self.nr_prob
    
    '''
    Se returneaza o problema dupa numarul laboratorului
    '''
    def Get_Nr_Lab(self):
        return self.nr_lab
    
    '''
    Se returneaza o problema dupa descriere
    '''
    def Get_Description(self):
        return self.descriere
    
    '''
    Se returneaza o problema dupa deadline
    '''
    def Get_Deadline(self):
        return self.deadline
    
    '''
    Se actualizeaza numarul unei probleme
    '''
    def Set_Nr_Prob(self,new_prob):
        self.nr_prob = new_prob
        
    '''
    Se actualizeaza numarul unui laborator
    '''
    def Set_Nr_Lab(self,new_lab):
        self.nr_lab = new_lab
        
    '''
    Se actualizeaza descrierea unei probleme
    '''
    def Set_Description(self,new_descriere):
        self.descriere = new_descriere
        
    '''
    Se actualizeaza deadline-ul unei probleme
    '''
    def Set_Deadline(self,new_deadline):
        self.deadline = new_deadline
    
    '''
    Se afiseaza o problema pentru un student
    '''
    def Show_Prob(self):
        print("Problema "+str(self.nr_prob)+" din laboratorul "+str(self.nr_lab)+" si descrierea "+str(self.descriere)+" are deadline-ul setat la data de "+str(self.deadline)+".\n")
        print()
        
    

    '''
    Se returneaza problema
    '''
    def Get_Problem(self):
        a = Problema(self.nr_lab, self.nr_prob, self.descriere, self.deadline)
        return a

    
def testProblema():
    Prob  = Problema(4,13,'a,b','13/11/2015')
    assert Prob.Get_Nr_Prob() == 13
    assert Prob.Get_Nr_Lab() == 4
    assert Prob.Get_Description() == 'a,b'
    assert Prob.Get_Deadline() == '13/11/2015'
    
    Prob1 = Problema(7,2,'primele 2 puncte','20/11/2015')
    assert Prob1.Get_Nr_Prob() == 2
    assert Prob1.Get_Nr_Lab() == 7
    assert Prob1.Get_Description() == 'primele 2 puncte'
    assert Prob1.Get_Deadline() == '20/11/2015'
    
testProblema()
    