'''
@Author: Sankar
@Date: 2021-04-06 21:10:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-06 21:15:09
@Title :Test Clinical Management
'''
import pytest
from src.HospitalManagement import ClinicalManagement

def test_read_file():
    '''
        Description:
            Reads a file and checks whether the entries dictionary is populated
        Parameter:
            None
        Return:
            None
    '''
    clinic = ClinicalManagement()
    entriesPatient = clinic.get_entriesPatient()
    entriesDoctor = clinic.get_entriesDoctor()
    for i in entriesPatient:
        list = entriesPatient[i]
        assert len(list) == 2
    for i in entriesDoctor:
        list = entriesDoctor[i]
        assert len(list) == 5

def test_add_record():
    '''
    Description:
        Adds a record and checks whether the same is reflected in the dictionary
    Parameter:
        None
    Return:
        None
    '''
    clinic = ClinicalManagement()
    clinic.add_patient("Sankar", "91 7894561230", 26)
    entriesPatient = clinic.get_entriesPatient()
    for i in entriesPatient:
        list = entriesPatient[i]
        assert len(list) == 3

def test_make_appointment():
    '''
    Description:
        Adds a record and checks whether the same is reflected in the dictionary
    Parameter:
        None
    Return:
        None
    '''
    clinic = ClinicalManagement()
    patient_id = clinic.existing_patient("Selvi")
    clinic.make_an_appointment(patient_id, 5)
    entriesDoctor = clinic.get_entriesDoctor()
    for i in entriesDoctor:
        list = entriesDoctor[i]
        for j in range(len(list)):
            dict = list[j]
            if(dict['id'] == 5):
                assert len(dict['patientList']) == 2