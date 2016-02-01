'''
Created on Jan 3, 2016

@author: Tincarica
'''

from Domain.Problema import Problema

class RepositoryExceptionProb(Exception):
    def __str__(self):
        return "Datele introduse nu exista."
    
class FileProblemRep:
    def __init__(self,fileName):
        self.fileName = fileName
        self.probleme = {}
        self.loadFromFile()
        
    """
    Se incarca datele din fisier in memorie.
    """
    def loadFromFile(self):
        try:
            f = open(self.fileName,"r")
        except IOError:
            return []
        
        line = f.readline().strip()
        while line!= "":
            attrs = line.split(" ")
            pb    = Problema(attrs[0], attrs[1], attrs[2],attrs[3])
            self.probleme[len(self.probleme)] = pb
            line  = f.readline().strip()
        f.close()
        #return self.students

    """
    Se salveaza datele din memorie in fisier.
    """
    def storeToFile(self):
        f = open(self.fileName,"w")
        for pb in self.probleme:
            #print(pb,type(stpb))
            strf = str(self.probleme[pb].Get_Nr_Lab()) + " " + str(self.probleme[pb].Get_Nr_Prob()) + " " + str(self.probleme[pb].Get_Description()) + " " + str(self.probleme[pb].Get_Deadline() )
            strf = strf + "\n"
            f.write(strf)
        f.close()
        
    def store(self,pb):
        allPbs = self.probleme
        #print(type(allStudents))
        if pb in allPbs:
            raise RepositoryExceptionProb
        #self.students[len(self.students)] = st
        self.storeToFile()
        
        
    
    '''
    Se salveaza o problema, daca nu exista deja.
    '''
    def Save_Problem(self,prob):
        for i in self.probleme:
            if self.probleme[i].Get_Nr_Lab() == prob.Get_Nr_Lab() and self.probleme[i].Get_Nr_Prob() == prob.Get_Nr_Prob():
                raise RepositoryExceptionProb
        self.probleme[len(self.probleme)] = prob
        self.storeToFile()
        
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
            if int(self.probleme[i].Get_Nr_Lab()) == int(nr_lab) and int(self.probleme[i].Get_Nr_Prob()) == int(nr_prob):
                self.probleme[i].Set_Description(descriere)
                self.probleme[i].Set_Deadline(deadline)
                self.storeToFile()
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
                self.storeToFile()
        if ok == 0:
            raise RepositoryExceptionProb

        
