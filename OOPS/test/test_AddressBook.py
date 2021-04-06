'''
@Author: Sankar
@Date: 2021-04-06 09:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-06 09:53:09
@Title : AddressBook Test
'''
import pytest
from AddressBook import Contact, AddressBook

def test_addressBook_add_entry():
    addressBook = AddressBook()
    contact = Contact("Sankar", "V", "9876543210", "abc@gmail.com")
    addressBook.add_entries(contact)
    entries = addressBook.get_entries()
    assert entries["Sankar"] == contact

def test_addressBook_remove_entry():
    addressBook = AddressBook()
    contact1 = Contact("Sankar", "V", "9876543210", "abc@gmail.com")
    addressBook.add_entries(contact1)
    contact2 = Contact("Selva", "V", "9876543210", "abc100@gmail.com")
    addressBook.add_entries(contact2)
    addressBook.remove_entry("Selva")
    entries = addressBook.get_entries()
    assert len(entries) == 1

def test_addressBook_update_entry():
    addressBook = AddressBook()
    contact = Contact("Sankar", "V", "9876543210", "abc@gmail.com")
    addressBook.add_entries(contact)
    addressBook.update_entry("Sankar", 2, "Vijaya")
    entries = addressBook.get_entries()
    assert entries["Sankar"].getLastName() == "Vijaya"