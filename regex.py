"""
Creating a fucntion (validatePhone) that takes one argument (value) and sees if it matches the appropriate
phone number format. Returns true and false otherwise.
"""
import re 

def validatePhone(value):
    """
    Checks to see if phone number is formatted with three digits followed 
    by a hyphen followed by 3 digits and then a hyphen with four digits after it 
    """
    phoneNumOne = re.compile('^[0-9]{3}-[0-9]{3}-[0-9]{4}$')
    #Checks to see if phone number is formatted with three digits followed by a hyphen and four digits after it
    phoneNumTwo = re.compile('^[0-9]{3}-[0-9]{4}$')
    """
    Checks to see if phone number is formatted with three digits in between round brackets followed by three
    digits, then a hyphen and then four more digits after it
    """
    phoneNumThree = re.compile('^([0-9]{3})[0-9]{3}-[0-9]{4}$')
    #Usinf if-else statements to see if the phone number matches the requirements and returns true or false otherwise
    if phoneNumOne.search(value) or phoneNumTwo.search(value) or phoneNumThree.search(value):
        return True
    else:
        return False

#Testing the validatePhone function
phoneNumber1 = '721-8668'
phoneNumber2 = '905-721-8668'
phoneNumber3 = '(905)721-8668'
phoneNumber4 = '9057218668'

print("Phone number " + phoneNumber1 + ":", validatePhone(phoneNumber1)) 
print("Phone number " + phoneNumber2 + ":", validatePhone(phoneNumber2)) 
print("Phone number " + phoneNumber3 + ":", validatePhone(phoneNumber3)) 
print("Phone number " + phoneNumber4 + ":", validatePhone(phoneNumber4))

"""
Part 2:
Creating a function (validateDomain) that takes one argument and returns true if it matches the domain
requirements. A lowercase string followed by an optional dot with lowercase,digits, or underscore, followed
by a dot and then either a com, ca or org.
"""
import re  
def validateDomain(value):
    #Using regex to see if domain meets requirements and ends with com
    domain = re.compile('^[a-z]+(.([a-z0-9_])*.)?.com$')
    #Using regex to see if domain meets requirements and ends with ca
    domain2 = re.compile('^[a-z]+(.([a-z0-9_])*.)?.ca$')
    #Using regex to see if domain meets requirements and ends with org
    domain3 = re.compile('^[a-z]+(.([a-z0-9_])*.)?.org$')
    #Usinf if-else statements to check if the domain matches with the requirements and returns true, and false otherwise
    if domain.search(value) or domain2.search(value) or domain3.search(value):
        return True
    else:
        return False
#Testing the validateDomain function
domainOne = 'google.ca'
domainTwo = 'animals.amazon.com'
domainThree = 'redcross.org'
domainFour = 'food.ag'
print()
print("Domain: " + domainOne, validateDomain(domainOne))
print("Domain: " + domainTwo, validateDomain(domainOne))
print("Domain: " + domainThree, validateDomain(domainOne))
print("Domain: " + domainFour, validateDomain(domainOne))

"""
Part 3:
Creating a function that retruns true if string contains  an even number of a's (including zero),
followed by any number of b's, followed by n c's where n is a multiple of 3. 
"""
def validateLang(value):
    #Using the regex to see if there are an even number of a's (0 or more) 
    #followed by any number of bs and c's that are a multiple of 3
    description = re.compile('(aa)*(bbb)*(ccc)*')
    if description.search(value):
        return True
    else:
        return False
#Testing the validateLang function
print("String bbcccc:", validateLang('abbcccc')) 
print("String aaaaccc:", validateLang('aaaaccc'))  
print("String aabbbbbcccccc:", validateLang('aabbbbbcccccc')) 
print("String abbcc:", validateLang('abbcc'))

"""
Part 4: 
Creating a fucntion (trimSpaces) that takes a single argument and replaces the white spaces
in the string to a single space
"""
print('\nPart 4')
def trimSpaces(value):
    #Removing the whitespaces in beginning and end of string
    removeSpace = value.strip()
    #Using the re.sub() to replace all white spaces in between the string to a single space
    whiteSpace = re.sub(' +', " ", removeSpace)
    #returning the new string 
    return whiteSpace

#Testing the trimSpaces function
print(" bbb ccc: " + trimSpaces(' bbb ccc')) 
print("bbb ccc :" + trimSpaces('bbb ccc '))
print("bbb ccc:" + trimSpaces('bbb ccc')) 
print(" bbb ccc :" + trimSpaces(' bbb ccc '))





    


