import string 
  
def pangram(sr): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in sr.lower(): 
            return False
  
    return True
      
# Driver code 
string = input()
if(pangram(string) == True): 
    print("yes") 
else: 
    print("no") 
