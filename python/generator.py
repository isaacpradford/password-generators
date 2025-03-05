# Requirements: 
# Generates n length of password
# No duplicate characters
# No two same characters next to each other
# Include special characters, capital letters, lowercase letters, and a number
# Min length of 8

import string
import random

###########################################
################## Try 1 ##################
###########################################

# Generates a password with n length without duplicate chars but doesn't guarantee special characters / capital / lowercase chars are included

# def generatePassword( charCount ) : 
#     if charCount < 8 :
#         print("PW must be longer than 8 characters")
#         return
    
#     chars = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list(string.punctuation)
#     pwRange = random.sample(range(1, len(chars)), charCount)
#     pw = ""
    
#     for i in pwRange : 
#         pw += chars[i]
    
#     return pw
        
        
        
###########################################
################## TRY 2 ##################
###########################################

# Closer, but by putting it into a set and not removing the character, it has to randomly search until it finds a character that doesn't match. 
# That's fine when it's 10 characters, but at 93 out of 94 characters, it has to do a lot of random searching

# So instead, we're going to ditch the set and just do a string. Since removing an index is 0(1), we'll pop the item that's at the rand index and then there's no way for it to duplicate

# def generatePassword ( charCount ) :
#     upper = list(string.ascii_uppercase)
#     lower = list(string.ascii_lowercase)
#     nums = list(string.digits)
#     punc = list(string.punctuation)
    
#     pw = set({})
#     charSets = [upper, lower, nums, punc]
    
#     if charCount > len(upper) + len(lower) + len(nums) + len(punc): 
#         print("Char count must not be larger than possible length of combined chars:", len(upper) + len(lower) + len(nums) + len(punc))
#         return
    
#     while charCount > len(pw):
#         randCharSet = random.choice(charSets)
#         randInt = random.sample(range(0, len(randCharSet)), 1)
#         pw.add(randCharSet[randInt[0]])

#         print(pw)
#         if charCount < len(pw) :
#             break

#     return "".join(pw)


        
###########################################
################## TRY 3 ##################
###########################################

# Almost there but doesn't currently guarantee that it will have a Special Character, Uppercase, Lowercase, and Digit
# def generatePassword ( charCount ) : 
#     upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     punc = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    
#     # charSets = [upper, lower, nums, punc]
#     charSets = [upper]
#     pw = ""

#     if charCount > len(upper) + len(lower) + len(nums) + len(punc): 
#         print("Char count must not be larger than possible length of combined chars:", len(upper) + len(lower) + len(nums) + len(punc))
#         return
     
#     while charCount > len(pw): # While the charcount requested is less than the length of the current pw
#         randCharSet = random.choice(charSets) # Grab a random set of characters
#         randInt = random.randint(0, len(randCharSet) - 1) # Grab a random index from the charset, -1 so it doesn't ever go past the bounds (EX: upper.len = 26, [26] is the 27th index)
        
#         pw = pw + randCharSet[randInt] # Add that letter to the pw
#         randCharSet.pop(randInt) # Remove that letter from the list of possible chars
        
#         print(len(randCharSet) )
        
#         if charCount < len(pw) : # End the loop once it's long enough
#             break
        
#     return pw

###################################################
################## TRY 4 / FINAL ##################
###################################################

def generatePassword ( charCount ) : 
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    punc = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    
    charSets = [upper, lower, nums, punc]
    pw = ""

    if charCount > len(upper) + len(lower) + len(nums) + len(punc): 
        return
     
    while charCount > len(pw): # While the charcount requested is less than the length of the current pw
        if (len(charSets) == 0) :
            if (len(upper) > 0) : 
                charSets.append(upper)
            if (len(lower) > 0) : 
                charSets.append(lower)
            if (len(nums) > 0) : 
                charSets.append(nums)
            if (len(punc) > 0) : 
                charSets.append(punc)

            
        randSetInt = random.randint(0, len(charSets) - 1) # Get random # from 0 - length of charSets currently
        randCharInt = random.randint(0, len(charSets[randSetInt]) -1 ) # Grab a random index from the charset, -1 so it doesn't ever go past the bounds (EX: upper.len = 26, [26] is the 27th index)
        
        pw = pw + charSets[randSetInt][randCharInt] # Add that letter to the pw
        
        charSets[randSetInt].pop(randCharInt) # Remove that letter from the list of possible chars
        charSets.pop(randSetInt)
        
    return pw


###################################################
################## TRY 5 / OOP ####################
###################################################

class Password :
    # Initialize class
    def __init__ ( self ):
        self.upper = list(string.ascii_uppercase)
        self.lower = list(string.ascii_lowercase)
        self.nums = list(string.digits)
        self.punc = list(string.punctuation)
        self.password = ""
    
    # Generate a password that matches requirements
    def generatePassword (self, charCount) :
        if (charCount < 8) :
            return
        elif charCount > len(self.upper) + len(self.lower) + len(self.nums) + len(self.punc): 
            return
        
        
        charSets = [self.upper, self.lower, self.nums, self.punc]
        pw = ""
        
        while charCount > len(pw): # While the charcount requested is less than the length of the current pw
            if (len(charSets) == 0) :
                if (len(self.upper) > 0) : 
                    charSets.append(self.upper)
                if (len(self.lower) > 0) : 
                    charSets.append(self.lower)
                if (len(self.nums) > 0) : 
                    charSets.append(self.nums)
                if (len(self.punc) > 0) : 
                    charSets.append(self.punc)

                
            randSetInt = random.randint(0, len(charSets) - 1) # Get random # from 0 - length of charSets currently
            randCharInt = random.randint(0, len(charSets[randSetInt]) -1 ) # Grab a random index from the charset, -1 so it doesn't ever go past the bounds (EX: upper.len = 26, [26] is the 27th index)
            
            pw = pw + charSets[randSetInt][randCharInt] # Add that letter to the pw
            
            charSets[randSetInt].pop(randCharInt) # Remove that letter from the list of possible chars
            charSets.pop(randSetInt)
            
        self.password = pw
    

###################################################
#####################  TESTS  #####################
###################################################

if __name__ == '__main__':
    pw = generatePassword(20)
    print(pw, len(pw))
    
    pw2 = Password()
    pw2.generatePassword(20)
    print(pw2.password, len(pw2.password))