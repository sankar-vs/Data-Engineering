'''
@Author: Sankar
@Date: 2021-04-06 21:10:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-06 21:15:09
@Title :Clinical Management
'''
import os, re
import logging, json

class ClinicalManagement:
    '''
    Class:
        ClinicalManagement

    Description:
        Class to maintain the data of Doctors and Patient, make an appointment with the doctor
        if there is a slot available

    Functions:
        add_patient(name, phone, age)
        existing_patient(name)
        print_doctor()
        print_patient()
        make_an_appointment(patient_id, doctor_id)

    Variable:
        entriesPatient (dict)
        entriesDoctor (dict)
    '''
    entriesDoctor = {}
    entriesPatient = {}

    def __init__(self):
        if os.path.isfile("resources/doctor.json"):
            with open("resources/doctor.json", "r") as f:
                self.entriesDoctor = json.load(f)
        if os.path.isfile("resources/patient.json"):
            with open("resources/patient.json", "r") as f:
                self.entriesPatient = json.load(f)

    def add_patient(self, name, phone, age):
        '''
        Description:
            adds the patient details
        Parameter:
            name(str) -> input from user
            phone (str) -> input from user
            age (int) -> input from user
        Return: 
            None
        '''
        for i in self.entriesPatient:
            list = self.entriesPatient[i]
            dict = {}
            dict['name'] = name
            dict['id'] = len(list) + 1
            dict['phone'] = phone
            dict['age'] = age
            list.append(dict)

    def existing_patient(self, name):
        '''
        Description:
            checks the patient name is present and if present returns patients id
        Parameter:
            name(str) -> input from user
        Return: 
            id (int)
        '''
        for i in self.entriesPatient:
            list = self.entriesPatient[i]
            for j in range(len(list)):
                dict = list[j]
                if (dict['name'] == name):
                    return dict['id']

    def print_doctor(self):
        '''
        Description:
            Prints doctor detials
        Parameter:
            None
        Return: 
            None
        '''
        for i in self.entriesDoctor:
            list = self.entriesDoctor[i]
            for j in range(len(list)):
                dict = list[j]
                print("------------------------------------------")
                print("name: {}".format(dict['name']))
                print("id: {}".format(dict['id']))
                print("Patient Waiting List: {}".format(dict['patientList']))
                print("availability: {}".format(dict['availability']))
                print("------------------------------------------")

    def print_patient(self):
        '''
        Description:
            Prints patient details
        Parameter:
            None
        Return: 
            None
        '''
        for i in self.entriesPatient:
            list = self.entriesPatient[i]
            for j in range(len(list)):
                dict = list[j]
                print("------------------------------------------")
                print("name: {}".format(dict['name']))
                print("id: {}".format(dict['id']))
                print("------------------------------------------")

    def make_an_appointment(self, patient_id, doctor_id):
        '''
        Description:
            Appends the patient_id to the doctor patient waiting list
        Parameter:
            patient_id (int) 
            doctor_id (int) 
            age (int)
        Return: 
            None
        '''
        for i in self.entriesDoctor:
            list = self.entriesDoctor[i]
            for j in range(len(list)):
                dict = list[j]
                if(dict['id'] == doctor_id):
                    if(len(dict['patientList']) < 6):
                        dict['patientList'].append(patient_id)
                        print("Appointment made")
                    else:
                        print("Sorry the slots are full")              

    def save_to_json(self):
        '''
        Description:
            Saves to JSON file
        Parameter:
            None
        Return: 
            None
        '''
        with open("resources/doctor.json", "w") as f:
                json.dump(self.entriesDoctor, f, indent=4)

        with open("resources/patient.json", "w") as f:
                json.dump(self.entriesPatient, f, indent=4)

    def get_entriesPatient(self):
        return self.entriesPatient

    def get_entriesDoctor(self):
        return self.entriesDoctor

def name_regex(x):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
    Parameter:
        x (str): Statement to be asked
    Return:
        name (str): input from user
    '''
    while True:
        try:
            name = input(x)
            pattern = "^[A-Z]{1}[a-zA-Z]{2,}$"
            result = re.match(pattern, name)
            if (result):
                return str(name)
        except:
            pass
        logging.warning("Enter proper Name")

def age_regex(x):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
    Parameter:
        x (str): Statement to be asked
    Return:
        age (int): input from user
    '''
    while True:
        try:
            age = input(x)
            pattern = "^([1-9][0-9]{,8})$"
            result = re.match(pattern, age)
            if (result):
                return int(age)
        except:
            pass
        logging.warning("Enter positive Integer")

def phone_regex(x):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
    Parameter:
        x (str): Statement to be asked
    Return:
        phone (str): input from user
    '''
    while True:
        try:
            phone = input(x)
            pattern = "^[0-9]{2}\\s[0-9]{10}$"
            result = re.match(pattern, phone)
            if (result):
                return str(phone)
        except:
            pass
        logging.warning("Enter proper Number")

def clinic_process():
    '''
    Description:
        Gives choice to user to perform features available from ClinicManagement class
    Parameter:
        None
    Return:
        None
    '''
    try:
        clinic = ClinicalManagement()
        user_input = ""

        while user_input != 'q':
            print("1 - New Patient")
            print("2 - Existing Patient")
            print("3 - Doctor List")
            print("4 - Write to File")
            print("q - Quit")
            user_input = input("Select Option: ")

            if (user_input == "1"):
                name = name_regex("Enter patients name: ")
                phone = phone_regex("Enter patients number: ")
                age = age_regex("Enter patients age: ")
                clinic.add_patient(name, phone, age)
                patient_id = clinic.existing_patient("Sankar")
                clinic.print_patient()
                clinic.print_doctor()
                choose_id = int(input("Please choode the ID of doctor you would like to consult: "))
                clinic.make_an_appointment(patient_id, choose_id)

            elif (user_input == "2"):
                patient_id = clinic.existing_patient("Selvi")
                clinic.print_patient()
                clinic.print_doctor()
                choose_id = int(input("Please choode the ID of doctor you would like to consult: "))
                clinic.make_an_appointment(patient_id, choose_id)

            elif (user_input == "3"):
                clinic.print_doctor()

            elif (user_input == "4"):
                clinic.save_to_json()

            elif (user_input == "q"):
                break

            else:
                print("Choose Options Properly")
    except:
        pass

clinic_process()