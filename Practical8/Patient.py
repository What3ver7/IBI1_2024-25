# Define a class named 'patients' with four attributes: name, age, date, and history.
# Create an initializer method __init__ that takes four parameters to initialize the class attributes.
# name: the patient's name
# age: the patient's age
# date: the date of the patient's latest admission
# history: the patient's medical history
# Define a method named 'date_time' that returns a formatted string of the latest admission date.
# Define a method named 'medical_history' that returns a formatted string of the medical history.
# Define a method named 'print' that returns a formatted string containing the patient's name, age, admission date, and medical history.
# Prompt the user to input the patient's name, age, date of latest admission, and medical history.
# Create an instance of the 'patients' class with the provided user inputs.
# print the result

class patients:
    def __init__(self,name,age,date,history):
        self.name=name
        self.age=age
        self.date=date
        self.history=history

    def date_time(self):
        return f"The date of latest admission is {self.date}"
    
    def medical_history(self):
        return f"{self.name}'s medical history is {self.history}"
    
    def print(self):
        return f"{self.name},{self.age},{self.date_time()},{self.medical_history()}."

name="Greenwood"
age="22"
date="2025.4.8"
history="None"
patient=patients(name,age,date,history)
print(patient.print())

#Example
"""
name=Greenwood
age=22
date=2025.4.8
medical history=None
print: Greenwood,22,The date of latest admission is 2025.4.8,Greenwood's medical history is None.
"""