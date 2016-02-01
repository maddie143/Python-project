'''
Created on Nov 25, 2015

@author: Mada
'''

from Repository.StudentRepository import StudentRepository
from Repository.ProblemRepository import ProblemRepository
from Controller.StudentController import StudentController
from Controller.ProblemController import ProblemController
from Repository.NoteRepository import NoteRepository
from Controller.NoteController import NoteController
from UI import Consola
from Repository.FileStudentRep import FileStudentRep
from Repository.FileProblemRep import FileProblemRep
from Repository.FileNoteRep import FileNoteRep

#RepStud   = StudentRepository()
#RepProb   = ProblemRepository()
#RepNote   = NoteRepository()
RepStud   = FileStudentRep("testSt.txt")
RepProb   = FileProblemRep("testPb.txt")
RepNote   = FileNoteRep("testNt.txt",RepStud)

ContrStud = StudentController(RepStud)
ContrProb = ProblemController(RepProb)
ContrNote = NoteController(RepNote,RepStud)

meniu     = Consola.Console(ContrStud,ContrProb,ContrNote)
meniu.ShowUI()

