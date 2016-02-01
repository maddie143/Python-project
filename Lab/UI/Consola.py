'''
Created on Nov 26, 2015

@author: Mada
'''
from Repository.StudentRepository import RepositoryExceptionStud
from Domain.Validator import ValidatorException, ValidatorProblema,\
    ValidatorStudent
from UI import Meniuri
from Repository.ProblemRepository import RepositoryExceptionProb
from Domain.Problema import Problema
from Domain.Student import Student
from Repository.FileStudentRep import FileStudentRep, RepositoryFileException,RepositoryExceptionStud
from Repository.FileProblemRep import FileProblemRep,RepositoryExceptionProb
from Repository.FileNoteRep import FileNoteRep
from Domain.Note import Note

class Console:
    """
    ctrS = StudentController
    ctrP = ProblemController
    ctrN = NoteController
    """
    def __init__(self, ctrS, ctrP, ctrN):
        self.ctrS = ctrS
        self.ctrP = ctrP
        self.ctrN = ctrN

    """
    Meniul studentilor
    """
    def MeniuStudent(self):
        ok = True
        while ok:
            Meniuri.Meniu_Student()
            comanda = input('Alegeti optiunea: ')
            if   comanda == '1':
                self.C_AddStudent()
            elif comanda == '2':
                self.C_AfisareStudenti()
            elif comanda == '3':
                self.C_DeleteStudent()
            elif comanda == '4':
                self.C_UpdateStudent()
            elif comanda == '5':
                self.C_FindStudent()
            elif comanda == '0':
                ok = False
                print("0")
            else:
                print ('Optiune invalida!')
                print()
                
    """
    Meniul Problemelor
    """
    def MeniuProblema(self):
        ok = True
        while ok:
            Meniuri.Meniu_Laborator()
            comanda = input('Alegeti optiunea: ')
            if   comanda == '1':
                self.C_AddProblema()
            elif comanda == '2':
                self.C_AfisareProbleme()
            elif comanda == '3':
                self.C_DeleteProblema()
            elif comanda == '4':
                self.C_UpdateProblema()
            elif comanda == '5':
                self.C_FindProblema()
            elif comanda == '0':
                ok = False
                print("1")
            else:
                print ('Optiune invalida!')
                print()
                
    '''
    Meniul pentru Statistici
    '''
    def MeniuStat(self):
        ok = True
        while ok:
            Meniuri.Meniu_Statistici()
            comanda = input('Alegeti optiunea: ')
            if comanda == '1':
                self.C_AfisareDateProb()
            elif comanda == '2':
                self.C_AfisareNoteAlf()
            elif comanda == '3':
                self.C_AfisareNoteCresc()
            elif comanda == '4':
                self.C_AfisareNote5()
            elif comanda == '0':
                ok = False
                print("3")
            else:
                print ('Optiune invalida!')
                print()
                
    """
    Meniul principal
    """
    def ShowUI(self):
        ok = True
        while ok:
            Meniuri.Meniu_Principal()
            comanda = input('Alegeti optiunea: ')
            if   comanda == '1':
                self.MeniuStudent()
            elif comanda == '2':
                self.MeniuProblema()
            elif comanda == '3':
                self.C_AssLab()
            elif comanda == '4':
                self.MeniuStat()
            elif comanda == '0':
                ok = False
            else:
                print ('Optiune invalida!')
                print()

    """
    Adaugare student            
    """
    def C_AddStudent(self):
        nume  = input("Numele studentului:")
        grupa = input("Grupa studentului:")
        print()
        try:
            nes = Student(nume,grupa,len(self.ctrS.repository.students))
            #ValidatorStudent(nes).Validate_Student()
            self.ctrS.AddStudent(nume,grupa)
            
            #Se salveaza in fisier
            m = FileStudentRep("testSt.txt")
            m.store(nes)
            
            print("Studentul a fost adaugat.")
            print()
            
        except RepositoryExceptionStud:
            print("Studentul cu datele precizate exista deja.")
            print()
        except ValidatorException as e:
            print("Au aparut erorile urmatoare: " + str(e))
            print()
        except RepositoryFileException:
            print("Studentul adaugat exista deja in baza de date.")
            print()
            
    """
    Stergere student
    """
    def C_DeleteStudent(self):
        stud = self.ctrS.GetStudents()
        if len(stud) > 0:
            print("Alegeti ID-ul studentului pe care doriti sa il stergeti:")
            print()
            for i in stud:
                print(str(i.Get_Stud_Name()) + "  " +str( i.Get_Stud_Group()) + "  " + str(i.Get_Stud_ID()))
            print()
            delID = input("Introduceti ID-ul studentului:")
            print()
            try:
                delID = int(delID)
                self.ctrS.DeleteStudent(delID)
                print("Studentul a fost sters.")
                print()
            except ValidatorException as e:
                print(e.__str__())
                print()
            except RepositoryExceptionStud:
                print("Nu exista studentul cu acel ID")
                print()
            except ValueError:
                print("ID incorect.")
                print()
        else:
            print("Nu exista studenti in repository.")
            print()
        
    """
    Se actualizeaza datele unui student
    """
    def C_UpdateStudent(self):
        stud = self.ctrS.GetStudents()
        if len(stud) > 0:
            print("Alegeti ID-ul studentului pe care doriti sa il actualizati:")
            print()
            for i in stud:
                print(str(i.Get_Stud_Name()) + "  " + str(i.Get_Stud_Group()) + "  " + str(i.Get_Stud_ID()))
            print()
            nId = input("Introduceti ID-ul:")
            print()
            try:
                nId   = int(nId)
                nume  = input("Numele nou:")
                grupa = input("Grupa noua:")
                print()
                self.ctrS.UpdateStudent(nume,grupa,nId)
                print("Studentul a fost modificat.")
                print()
            except ValidatorException as e:
                print("Au aparut erorile:" + e.__str__()) 
                print()
            except ValueError:
                print("ID incorect.")
                print()
        else:
            print("Nu exista studenti in repository.")
            print()
    
    """
    Cautare student
    """
    def C_FindStudent(self):
        stud = self.ctrS.GetStudents()
        if len(stud) > 0:
            name = input("Introduceti numele studentului cautat:")
            print()
            try:
                name.isalpha()
                stud = self.ctrS.FindStudentByName(name)
                print(str(stud.Get_Stud_Name()) + " este in grupa " + str(stud.Get_Stud_Group()) + " si are ID-ul " + str(stud.Get_Stud_ID())+".")
                print()
            except RepositoryExceptionStud:
                print("Studentul cu numele cautat nu exista.")
                print()
            except ValueError:
                print("Numele nu a fost dat corect.")
                print()
        else:
            print("Nu exista studenti in repository.")
            print()
            
    '''
    Se afiseaza studentii
    '''
    def C_AfisareStudenti(self):
        stud = self.ctrS.GetStudents()
        if len(stud) == 0:
            print("Nu exista studenti in repository.")
            print()
        else:
            for i in range(0,len(stud)):
                print("Nume:" + str(stud[i].Get_Stud_Name()) + "   Grupa: " +str(stud[i].Get_Stud_Group()) + "    ID: " + str(stud[i].Get_Stud_ID()))
            print()
            
    '''
    Se adauga o problema noua
    '''
    def C_AddProblema(self):
        nr_lab    = input("Numarul laboratorului:")
        nr_prob   = input("Numarul problemei:")
        descriere = input("Descrierea problemei:")
        print("Deadlinul este de forma zz/mm/yy")
        deadline  = input("Deadline:")
        print()
        try:
            int(nr_lab)
            int(nr_prob)
            p = Problema(nr_lab,nr_prob,descriere,deadline)
            ValidatorProblema(p).Validate_Problem()
            self.ctrP.AddProblem(nr_lab,nr_prob,descriere,deadline)
            
            # Se salveaza in fisier
            m = FileProblemRep("testPb.txt")
            m.store(p)
            print("Problema a fost adaugata.")
            print()
        except ValidatorException as e:
            print("Au aparut urmatoarele erori: " + str(e))
            print()
        except RepositoryExceptionProb:
            print("Problema introdusa exista deja.")
            print()
        except ValueError:
            print("Datele introduse nu indeplinesc conditiile.")
            print()
            
    """
    Functia afiseaza toate problemele
    """
    def C_AfisareProbleme(self):
        probleme = self.ctrP.GetAllProblems()
        if len(probleme) == 0:
            print ('Nu exista probleme.')
            print()
        else:
            for i in range(0,len(probleme)):
                print("Nr_lab:" + str(probleme[i].Get_Nr_Lab()) + "   Nr_Prob: " +str(probleme[i].Get_Nr_Prob()) + "    Descriere: " + str(probleme[i].Get_Description()) + "     Deadline: " + str(probleme[i].Get_Deadline()))
            print()
            
    """
    Functia sterge o problema (data de nr_lab si nr_prob)
    """
    def C_DeleteProblema(self):
        probleme = self.ctrP.GetAllProblems()
        if len(probleme) > 0 :
            nr_lab  = input("Numarul laboratorului:")
            nr_prob = input("Numarul problemei:")
            print()
            try:
                int(nr_lab)
                int(nr_prob)
                #p = Problema(nr_lab,nr_prob,"a","11/11/2015")
                self.ctrP.DeleteProb(nr_lab,nr_prob)
                print("Problema a fost stearsa cu succes.")
                print()
            except RepositoryExceptionProb:
                print("Datele introduse nu exista.")
                print()
            except ValidatorException as e:
                print("Au aparut urmatoarele erori: " + e.__str__())
                print()
            except ValueError:
                print("Datele nu au fost introduse corect.")
                print()
        else:
            print("Nu exista probleme in repository.")
            print()
    
    '''
    Functia actualizeaza datele: descriere si deadline al unei probleme(dupa nr_lab, nr_prob)
    '''
    def C_UpdateProblema(self):
        probleme = self.ctrP.GetAllProblems()
        if len(probleme) > 0 :
            for i in range(0,len(probleme)):
                print("Nr lab: " +str(probleme[i].Get_Nr_Lab()) + "   Nr.Prob: " + str(probleme[i].Get_Nr_Prob()))
            print()
            nr_lab    = input("Numarul laboratorului:")
            nr_prob   = input("Numarul problemei:")
            descriere = input("Noua descriere:")
            deadline  = input("Noul deadline:")
            print()
            try:
                int(nr_lab)
                int(nr_prob)
                p = Problema(nr_lab,nr_prob,descriere,deadline)
                ValidatorProblema(p).Validate_Problem()
                self.ctrP.UpdateProb(nr_lab,nr_prob,descriere,deadline)
                print("Problema a fost modificata.")
                print()
            except RepositoryExceptionProb:
                print("Problema cu datele respective nu exista in baza de date.")
                print()
            except ValidatorException as e:
                print("Au aparut urmatoarele erori:"+ str(e))
                print()
            except ValueError:
                print("Datele introduse nu corespund cerintelor (nr_lab si nr_prob de tip int).")
                print()
            except KeyError:
                print("Tipul datelor comparate nu coincid.")
                print()
        else:
            print("Nu exista probleme in repository.")
            print()
            
    """
    Se cauta o problema dupa nr_lab si nr_prob
    """
    def C_FindProblema(self):
        probleme = self.ctrP.GetAllProblems()
        if len(probleme) > 0 :
            for i in range(0,len(probleme)):
                print("Nr.Lab:" + str(probleme[i].Get_Nr_Lab()) + "   Nr.Prob: "+ str(probleme[i].Get_Nr_Prob()))
            print()
            nr_lab    = input("Numarul laboratorului:")
            nr_prob   = input("Numarul problemei:")
            print()
            try:
                int(nr_lab)
                int(nr_prob)
                new = self.ctrP.FindProb(nr_lab, nr_prob)
                print("Nr.Lab:" + str(new.Get_Nr_Lab()) + "   Nr.Prob: "+ str(new.Get_Nr_Prob()) + "   Descriere: " + str(new.Get_Description()) + "    Deadline: " + str(new.Get_Deadline()))
                print()
            except RepositoryExceptionProb:
                print("Nu exista o problema cu datele respective in repository.")
                print()
            except ValueError:
                print("Datele introduse nu indeplinesc conditiile.")
                print()
        else:
            print("Nu exista probleme in repository.")
            print()

    '''
    Functia asigneaza o nota unei probleme a unui student
    '''
    def C_AssLab(self):
        m    = self.ctrS.GetStudents()
        for i in range(0,len(m)):
            print("Studentul: ",m[i].Get_Stud_Name())
        print()
        
        nume = input("Numele studentului:")
        prob = input("Problema:")
        nota = input("Nota:")
        print()
        
        try:
            nume.isalpha()
            int(prob)
            int(nota)
            st = self.ctrS.ret_st_name(nume)
            pb = self.ctrP.ret_pb_nrpb(prob)
            nes = Note(st,pb,nota)
            self.ctrN.AddNota(nume,prob,nota)
            print("Nota a fost asignata cu succes.")
            print()
            
            #Se salveaza in fisier
            m = FileNoteRep("testNt.txt",self.ctrS.repository)
            m.store(nes)
            
        except ValueError:
            print("Una dintre date nu a fost introdusa corect.")
            print()
        except ValidatorException as e:
            print("Datele introduse nu corespund cerintelor" + e.__str__())
            print()
        except RepositoryExceptionStud:
            print("Studentul cu numele dat nu exista.")
            print()
            
    '''
    Functia afiseaza lista studentilor ordonata dupa nume
    '''
    def C_AfisareNoteAlf(self):
        note = self.ctrN.GetNote()
        for i in range(0,len(note)):
            for j in range(0,len(note)):
                if str(note[i].Get_Stud().Get_Stud_Name()) < str(note[j].Get_Stud().Get_Stud_Name()):
                    aux     = note[i]
                    note[i] = note[j]
                    note[j] = aux
        for i in range(0,len(note)):
            ok = 1
            for j in range(0,i):
                if str(note[i].Get_Stud().Get_Stud_Name()) == str(note[j].Get_Stud().Get_Stud_Name()):
                    ok = 0
            if ok == 1:
                print("Studentul ",str(note[i].Get_Stud().Get_Stud_Name()),".")
            #print("Studentul ",str(self.ctrN.GetNote[i].Get_Stud())," are nota ",str(self.ctrN.GetNote[i].Get_Nota())," pe problema ",str(self.ctrN.GetNote[i].Get_Prob()),".")
        print()
    
    '''
    Functia afiseaza lista studentilor ordonata dupa note
    '''
    def C_AfisareNoteCresc(self):
        note = self.ctrN.GetNote()
        for i in range(0,len(note)):
            for j in range(i,len(note)):
                if int(note[i].Get_Nota()) < int(note[j].Get_Nota()):
                    aux     = note[i]
                    note[i] = note[j]
                    note[j] = aux
        for i in range(0,len(note)):
            print("Studentul ",str(note[i].Get_Stud().Get_Stud_Name())," are nota ",note[i].Get_Nota()," pe problema ",str(note[i].Get_Prob()),".")
        print()
        
    '''
    Functia afiseaza lista studentilor care au media notelor cel mult 5
    '''
    def C_AfisareNote5(self):
        note     = self.ctrN.GetNote()
        students = self.ctrS.GetStudents()
        ok = 0
        for i in range(0,len(students)):
            S  = 0
            nr = 0
            for j in range(0,len(note)):
                if note[j].Get_Stud().Get_Stud_Name() == students[i].Get_Stud_Name():
                    S  = S + int(note[j].Get_Nota())
                    nr = nr + 1
            p = S/nr
            if p <= 5 :
                print("Studentul ", students[i].Get_Stud_Name()," are media laboratoarelor mai mica decat 5.")
                ok = 1
        if ok == 0:
            print("Nu exist studenti cu media mai mica decat 5.")
        print()
    
    '''
    Functia afiseaza lista notelor unei probleme
    '''
    def C_AfisareDateProb(self):
        note = self.ctrN.GetNote()
        ask  = input("Problema cautata:")
        print()
        try:
            ok = 0
            int(ask)
            
            a = self.ctrN.GetProbsStud(ask)
            for i in range(0,len(a)):
                for j in range(0,len(note)):
                    if str(note[j].Get_Stud().Get_Stud_Name()) == str(a[i]) and int(note[j].Get_Prob()) == int(ask) :
                        print("Studentul ", note[j].Get_Stud().Get_Stud_Name(), " a primit nota ",note[j].Get_Nota()," pe problema cautata." )
                        ok = 1
                    
            if ok == 0:
                print("Nu exista note pe probleme respectiva.")
            print()
        except ValueError:
            print("Problema trebuie sa fie un integer.")
                

        
