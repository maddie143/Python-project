'''
Created on Nov 26, 2015

@author: Mada
'''
from Domain import Problema

class RepositoryExceptionProb(Exception):
    def __str__(self):
        return "Datele introduse nu exista."
    
class ProblemRepository:
    def __init__(self):
        self.probleme = {}
        
    '''
    Se salveaza o problema, daca nu exista deja.
    '''
    def Save_Problem(self,prob):
        
        for i in self.probleme:
            if self.probleme[i].Get_Nr_Lab() == prob.Get_Nr_Lab() and self.probleme[i].Get_Nr_Prob() == prob.Get_Nr_Prob():
                raise RepositoryExceptionProb
        self.probleme[len(self.probleme)] = prob
        
    '''
    Functia returneaza numarul de probleme
    '''
    def Nr_Problems(self):
        return len(self.probleme)
    
    '''
    Functia returneaza lista cu problemele
    '''
    def Get_Problems(self):
        return list(self.probleme.values())
    
    '''
    Functia returneaza o problema (cautata dupa nr_lab si nr_prob)
    '''
    def Find_By_Lab_Prob(self, nr_lab, nr_prob):
        for i in self.probleme:
            if self.probleme[i].Get_Nr_Lab() == nr_lab and self.probleme[i].Get_Nr_Prob() == nr_prob:
                return self.probleme[i]
        raise RepositoryExceptionProb()
    
    '''
    Functia actualizeaza datele: descriere si deadline al unei probleme cu datele:nr_lab, nr_prob
    '''
    def Update_Prob(self,nr_lab,nr_prob, descriere, deadline):
        ok   = 0
        nrpb = len(self.probleme)
        for i in range(0,nrpb):
            if self.probleme[i].Get_Nr_Lab() == nr_lab and self.probleme[i].Get_Nr_Prob() == nr_prob:
                self.probleme[i].Set_Description(descriere)
                self.probleme[i].Set_Deadline(deadline)
                ok = 1
        if ok == 0:
            raise RepositoryExceptionProb()
    
    '''
    Functia sterge o problema (dandu-se nr_lab si nr_prob)
    '''
    def Delete(self, nr_lab, nr_prob):
        nr = len(self.probleme)
        ok = 0
        for i in range(0,nr):
            if (self.probleme[i].Get_Nr_Lab() == nr_lab and self.probleme[i].Get_Nr_Prob() == nr_prob):
                ok = 1
                self.probleme.pop(i)
        if ok == 0:
            raise RepositoryExceptionProb
    
    
def TestSaveProb():
    rep   = ProblemRepository()
    
    prob  = Problema.Problema(4,3,'Number 1','5/5/2009')
    prob1 = Problema.Problema(4,1,'Number 2','5/5/2009')
    #assert rep.size() == 0
    try:
        rep.Save_Problem(prob)
        assert rep.Nr_Problems() == 1
        rep.Save_Problem(prob1)
        assert rep.Nr_Problems() == 2
    except RepositoryExceptionProb:
        print("Datele introduse deja exista.")
        
def TestUpdateProb():
    rep  = ProblemRepository()
    prob = Problema.Problema(4,3,'Incearca','5/5/2009')
    '''
    Se incearca salvarea datelor(daca nu exista deja se continua)
    '''
    try:
        rep.Save_Problem(prob)
        assert rep.Nr_Problems() == 1
        '''
        Se actualizeaza datele, daca exista, in caz contrar se afiseaza mesajul corespunzator.
        '''
        try : 
            rep.Update_Prob(4,3,'Merge','6/6/2003')
        except RepositoryExceptionProb:
            print("Datele introduse nu exista, deci nu pot fi actualizate.")
        
    except RepositoryExceptionProb:
        print("Datele introduse deja exista.")
    
def TestFindProb():
    rep   = ProblemRepository()
    prob  = Problema.Problema(4,3,'Prima','5/5/2009')
    prob1 = Problema.Problema(4,1,'A doua','5/5/2009')
    '''
    Se incearca salvarea celor doua probleme noi
    '''
    try:
        rep.Save_Problem(prob)
        rep.Save_Problem(prob1)
    except RepositoryExceptionProb:
        print("Datele introduse deja exista.")
    '''
    Se cauta problema cu datele mentionate
    '''
    try:
        rep.Find_By_Lab_Prob(4,1)
        assert rep.Find_By_Lab_Prob(4,1) == prob1
    except RepositoryExceptionProb:
        print("Problema cu datele precizate nu exista in repository.")
    

TestSaveProb()
TestUpdateProb()
TestFindProb()