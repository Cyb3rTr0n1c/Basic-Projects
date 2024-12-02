#Daniel Torres Montoya 27/08/2024

import string
import re
import math
from getpass import getpass



def categorizedScore(score):
	if score > 23:
		print ("Very strong password")
		print(score)
	elif score >18:
		print("Strong password")
		print(score)
	elif score > 13:
		print("Moderate password")
		print(score)
	elif score > 8:
		print("Weak password")
		print(score)
	else:
		print("Very weak password")
		print(score)

def passwordtester(inputPassword):
	totalScore = 0
	totalScore += int(lengthChecker(inputPassword))
	totalScore += int(varietyChecker(inputPassword))
	totalScore += int(patternChecker(inputPassword))
	totalScore += int(entropyChecker(inputPassword))
	categorizedScore(totalScore)

def lengthChecker(inputPassword):
	lengthScore = 0

	if len(inputPassword)>20:
		lengthScore+=7
	elif len(inputPassword)>15:
		lengthScore+=5
	elif len(inputPassword)>10:
		lengthScore+=3
	elif len(inputPassword)>7:
		lengthScore+=1
	else:
		lengthScore+=0

	return lengthScore

def varietyChecker(inputPassword):
	varietyScore = 0
	varietyQuantity = 0

	for i in string.ascii_lowercase:
		if i in inputPassword:
			varietyQuantity+=1
			break

	for i in string.ascii_uppercase:
		if i in inputPassword:
			varietyQuantity+=1
			break

	for i in string.digits:
		if i in inputPassword:
			varietyQuantity+=1
			break

	for i in '!@#$%^&*()_+-=[]{}|;:,.<>?':
		if i in inputPassword:
			varietyQuantity+=1
			break

	if varietyQuantity>3:
		varietyScore+=4

	elif varietyQuantity>2:
		varietyScore+=3

	elif varietyQuantity>1:
		varietyScore+=2
	
	else:
		varietyScore+=1

	return varietyScore

def patternChecker(inputPassword):
	patternScore = 0
	common_words = [
    "password", "admin", "letmein", "123456", "qwerty", "welcome", "123456789", "iloveyou", "abc123", "football", 
    "123123", "monkey", "starwars", "dragon", "hello", "princess", "superman", "sunshine", "master", "login", 
    "1234", "passw0rd", "trustno1", "batman", "whatever", "freedom", "secret", "qwertyuiop", "111111", "access", 
    "shadow", "michael", "baseball", "ninja", "test", "flower", "internet", "jesus", "liverpool", "charlie", 
    "welcome1", "987654321", "654321", "letmein123", "asdfgh", "tigger", "zxcvbnm", "000000", "summer", "buster"
	]
	keyboard_patterns = [
    "qwerty", "asdfgh", "zxcvbn", "12345", "qwertyuiop", "asdfghjkl", "zxcvbnm", "123456", "123456789", "1q2w3e", 
    "1qaz2wsx", "qazwsx", "qwer1234", "1q2w3e4r", "123qwe", "1q2w3e4r5t", "qwert", "q1w2e3r4", "q1w2e3", 
    "qwe123", "poiuytrewq", "mnbvcxz", "09876", "87654321", "qweasd", "1qazxsw2", "zxc123", "plmoknijb", 
    "wsxedc", "qaz123", "zaq12wsx", "321qwe", "qazwsxedc", "asdf1234", "654321", "asdfg123", "wertyu", "456789", 
    "qwert12345", "123asdf", "1q2w3e4r5", "asdfzxcv", "asdfgh123", "poiuyt", "2wsx3edc"
	]

	    
	for word in common_words:
		if word.lower() in inputPassword.lower():
			patternScore -= 5
			break  

	if re.search(r'(.)\1{2,}', inputPassword):
		patternScore -= 3

	sequences = ['0123456789', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'][::-1]
	for seq in sequences:
		for i in range(len(seq) - 3):
			if seq[i:i + 4] in inputPassword.lower():
				patternScore -= 3
				break
	for pattern in keyboard_patterns:
		if pattern in inputPassword.lower():
			patternScore -= 3
			break

	return patternScore



def entropyChecker(inputPassword):
    entropyScore = 0
    char_sets = {
        'lowercase': set(string.ascii_lowercase),
        'uppercase': set(string.ascii_uppercase),
        'digits': set(string.digits),
        'special': set('!@#$%^&*()_+-=[]{}|;:,.<>?')
    }

    used_chars = set(inputPassword)
    char_set_size = 0
    if any(c in char_sets['lowercase'] for c in used_chars):
        char_set_size += len(char_sets['lowercase'])
    if any(c in char_sets['uppercase'] for c in used_chars):
        char_set_size += len(char_sets['uppercase'])
    if any(c in char_sets['digits'] for c in used_chars):
        char_set_size += len(char_sets['digits'])
    if any(c in char_sets['special'] for c in used_chars):
        char_set_size += len(char_sets['special'])
    
    length = len(inputPassword)
    entropy = length * math.log2(char_set_size)
    
    if entropy < 28:
        entropyScore+= 1
    elif entropy < 40:
        entropyScore+= 4
    elif entropy < 56:
        entropyScore+= 6
    else:
        entropyScore+= 8

    return entropyScore


choice = 0
 
while choice !=3:
	choice = int(input("\nWhat do you want to do? \n 1-Check strength of the password \n 2-Learn about the scoring system \n 3-Close strength checker \n\n"))

	if choice>3 or choice<0:
		print("Type one of the numbers above (more choices will come with future updates)\n")
	elif choice == 1:
		passwordToTest = getpass("\nType your password to see its strength\n\n")
		passwordtester(passwordToTest)

	elif choice ==2:
		print("The password strength checker assigns points based on several criteria.\n") 
		print("Password length contributes up to 7 points: less than 8 characters scores 0, while more than 20 characters scores 7.\n") 
		print("Character variety adds up to 7 points, with more points for using uppercase, lowercase, numbers, and special characters.\n")
		print("Deductions are applied for common patterns like '1234' or 'password' (-5 points) and predictable sequences like 'abcd' or repeated characters (-3 points).\n")
		print("Entropy, which measures randomness, adds up to 8 points, with higher scores for unpredictable combinations.\n")
		print("The final score categorizes the password as very weak (0-5), weak (6-10), moderate (11-15), strong (16-20), or very strong (21+).\n")
		print("Updates to come: Personal information test before the strength checker, common password dictionaries, similarity substitution (3 = E, 0 = O, I = 1)")


