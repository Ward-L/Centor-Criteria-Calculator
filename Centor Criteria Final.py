#Centor Criteria Final
#This is a program that calculates the centor criteria guidelines for use of antibiotics in patients with tonsilitis.

import tkinter as tk
from tkinter import *
master = Tk()
master.title("Centor Criteria Calculator")
#This imports the module Tkinter which acts as the graphical user interface (GUI) for this calculator.

#These serve as the variables for each of the 4 criteria of the centor score (Absence of cough, fever present, tonsilar exudate presence and tender anterior cervical lymphadenopathy)
#Each one is assigned a value of 1 or 0 depending if a check box is checked in the definitions below.
coughgone = IntVar()
fever = IntVar()
exudate = IntVar()
tenderlymphnodes = IntVar()

#This is a code for the check box in which the clinician would tick if the patient as an absence of a cough. Doing so returns a value of "1" to the coughgone IntVar() above.
def coughabsence():
    Label(master, text="Is there a cough present?:").grid(row=0, sticky=W)
    Checkbutton(master, text="Cough Absent", onvalue=1, offvalue=0, variable=coughgone).grid(row=1, sticky=W)   

#This is a code for the check box in which the clinician would tick if the patient has a present fever. Doing so returns a value of "1" to the fever IntVar() above.
def feverpresent():
    Label(master, text="Is there a fever present (>38°C?):").grid(row=4, sticky=W)
    Checkbutton(master, text="Fever Present", onvalue=1, offvalue=0, variable=fever).grid(row=5, sticky=W)

#This is a code for the check box in which the clinician would tick if the patient has presence (on examination) or history of tonsiluar exudate.  Doing so returns a value of "1" to the exudate IntVar() above.
def exudatepresent():
    Label(master, text="Is there any tonsilar exudate (ooze)?:").grid(row=8, sticky=W)
    Checkbutton(master, text="Exudate Present", onvalue=1, offvalue=0, variable=exudate).grid(row=9, sticky=W)

#This is a code for the check box in which the clinician would tick if the patient has tender anterior cervical lymphadenopathy one examination or history. 
#Doing so returns a value of "1" to the tenderlymphnodes IntVar() above.
def tenderlymph():
    Label(master, text="Is there any tender anterior cervical lymphadenopathy?:").grid(row=12, sticky=W)
    Checkbutton(master, text="Tender anterior lymphadenopathy present", onvalue=1, offvalue=0, variable=tenderlymphnodes).grid(row=13, sticky=W)

#This codes for the calculation of the total centorscore (denoted as centorscore) - this is calculated based on the presence of fever, tender cervical lymph nodes, tonsiluar exudate and an absence of cough.
#Each of those values, if positive, return a value of "1". The total centor score is calculated by addin g these all together.
#This has been coded so this occurs when the button is clicked and prints the answer both on the GUI and in the terminal with reccomendations.
#>= 3 is used as this is the cut off according to NICE regulations.
def clicked():
    centorscore = coughgone.get() + fever.get() + exudate.get() + tenderlymphnodes.get()
    Centor_total_label = tk.Label(master, text = "The centor score is: ").grid(row=17, sticky = W)
    Centor_total_label2 = tk.Label(master, text = centorscore).grid(row=17, sticky = S)
    print ("Your centor score is:", centorscore)
    if centorscore >=3:
        antibiotics_label = tk.Label(master, text = "Antibiotics reccomended. Please consult antibiotic local guidelines.", bg="green", fg="white").grid(row=18, padx=10)
        print("Antibiotics reccomended. Please consult local antibiotics guidelines.")
    else:
        noantibiotics_label = tk.Label(master, text = "Antibiotics not reccomended. Consider rapid strep testing or culture.", bg="Red", fg= "White").grid(row=18)
        print("Antibiotics not reccomended. Consider rapid strep testing or culture.")   

#This codes for the button that when pressed with perform the click command above.
def calculate():
    Button(master, text="Calculate centor score", command=clicked).grid( row = 15, sticky=S, pady = 4)

#This exits the program.
def quit():
    Button(master, text='Quit', command=master.quit).grid(row=20, sticky=S, pady=4)


coughabsence()  
feverpresent()
exudatepresent()
tenderlymph()

calculate()

quit()

mainloop()