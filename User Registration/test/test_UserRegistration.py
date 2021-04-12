import pytest
import UserRegistration as ur

def test_checkGivenFirstNameIsValid():
    assert ur.name_regex("Samuel") == True

def test_checkGivenFirstNameIsNotValid_DoesNotStartWithCapital():
    assert ur.name_regex("samuel") == False

def test_checkGivenFirstNameIsNotValid_includesNumeric():
    assert ur.name_regex("Samuel123") == False

def test_checkGivenFirstNameIsNotValid_lessThan3Characters():
    assert ur.name_regex("Sa") == False

def test_checkGivenEmailIsValid():
    assert ur.email_regex("abc.100@gmail.com") == True

def test_checkGivenEmailNotValid():
    assert ur.email_regex("abc..100@gmail.com.") == False

def test_checkGivenPhoneNumberIsValid():
    assert ur.phone_regex("91 7894561230") == True

def test_checkGivenPhoneNumberNotValid_withoutSpace():
    assert ur.phone_regex("917894561230") == False

def test_checkGivenPhoneNumberNotValid_withoutLessThan10Digits():
    assert ur.phone_regex("91 789456123") == False

def test_checkGivenPhoneNumberNotValid_withoutMoreThan10Digits():
    assert ur.phone_regex("91 78945612300") == False

def test_checkGivenPhoneNumberNotValid_countryCodelessThan2Digits():
    assert ur.phone_regex("9 7894561230") == False

def test_checkGivenPasswordIsValid():
    assert ur.password_regex("S@muel123John") == True

def test_checkGivenPasswordNotValid_LessThan8Characters():
    assert ur.password_regex("Sam1") == False

def test_checkGivenPasswordNotValid_Atleast1orMoreCapitalLetter():
    assert ur.password_regex("awesomecode") == False

def test_checkGivenPasswordNotValid_Atleast1OrMoreNumeric():
    assert ur.password_regex("Awesomecode") == False

def test_checkGivenPasswordNotValid_Only1SpecialCharacter():
    assert ur.password_regex("P@@ce1234567") == False