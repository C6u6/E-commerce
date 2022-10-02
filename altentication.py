import re

# Check the username
def validusername(username):
    if username == "" or "@" in username:
        return False
    return True

# Check if a user name is valid
def validnames(name, surname):
    if name == "" or surname == "":
        return False
    if " " in surname:
        new_surname = surname.replace(" ", "a")
    else:
        new_surname = surname
    if not (name.isalpha()) or not (new_surname.isalpha()):
        return False
    return True

# Check password
def validpassword(password, confirmation, minsize=4, maxsize=None,
    upperletter=False, numbers=False, onlyletters=False):
    sizepass = len(password) 
    if maxsize == None:
        maxsize = sizepass

    if password != confirmation:
        return False
    if password == '':
        return False
    if sizepass < minsize or sizepass > maxsize:
        return False
    if upperletter == True:
        count = 0
        for char in password:
            charcopy = char.upper()
            if char == charcopy:
                count += 1

            if count == 0:
                return False
    if numbers == True:
        count = 0
        for char in password:
            if char.isnumeric():
                count += 1
        if count == 0:
            return False

    if onlyletters == True:
        if not (password.isalpha()):
            return False
    
    return True

def validemail(email):
    # Regex comes from https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/
    regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

    if re.fullmatch(regex, email):
        return True

    return False