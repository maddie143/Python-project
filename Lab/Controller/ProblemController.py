'''
Created on Nov 25, 2015

@author: Mada
'''
from Domain import Problema
from Domain.Validator import ValidatorProblema
from Repository import ProblemRepository

class ProblemController:
    def __init__(self,repository):
        self.repository = repository
    
    def AddProblem(self, nr_lab, nr_prob, descriere,deadline):
        new_prob = Problema.Problema(nr_lab, nr_prob,descriere, deadline)
        ValidatorProblema(new_prob)
        self.repository.Save_Problem(new_prob)
            
    """
    Returneaza toate problemele
    """
    def GetAllProblems(self):
        return self.repository.Get_Problems()
    
    """
    Se sterge o problema dupa numarul laboratorului si numarul problemei
    """
    def DeleteProb(self, nr_lab, nr_prob):
        self.repository.Delete(nr_lab,nr_prob)

            
    """
    Se actualizeaza o problema.
    Se verifica ca datele noi sa indeplineasca conditiile si ca problema (nr_lab,nr_prob)
    sa existe.
    """
    def UpdateProb(self,nr_lab,nr_prob,descriere,deadline):
        self.repository.Update_Prob(nr_lab,nr_prob,descriere,deadline)
        
    """
    Se cauta o problema dupa nr_lab si nr_prob
    """
    def FindProb(self,nr_lab,nr_prob):
        return self.repository.Find_By_Lab_Prob(nr_lab,nr_prob)
    
    def ret_pb_nrpb(self,nrpb):
        for i in self.repository.probleme:
            if self.repository.probleme[i].Get_Nr_Prob() == nrpb:
                return self.repository.probleme[i]
        return 0
            
        

        
def TestAddProb():
    
    rep       = ProblemRepository.ProblemRepository()
    contr     = ProblemController(rep)
    contr.AddProblem(4,3, 'aaa', '2/3/2000')
    prob     = Problema.Problema(4,3, 'aaa', '2/3/2000')
    probleme = contr.GetAllProblems()
    assert len(probleme) == 1
    assert probleme[0].Get_Nr_Lab() == prob.Get_Nr_Lab()

def TestDeleteProb():
    rep  = ProblemRepository.ProblemRepository()
    contr = ProblemController(rep)
    contr.AddProblem(4,3, 'aaa', '2/3/2000')
    contr.DeleteProb(4,3)
    probleme = contr.GetAllProblems()
    assert len(probleme) == 0
    
    
TestAddProb()
TestDeleteProb()
            
        
    
    
    
    
        
        
        