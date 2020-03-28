alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
input = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

#First Ceasar Cipher
#Function to decode input with specific offset

def decode(message, offset):
    result = []
    for x in message:
        ind = alphabet.find(x)
        if ind != -1:
            new_ind = ind + offset
            result.append(alphabet[new_ind])
        else:
            result.append(x)
    result = "".join(result)
    return result

print(decode(input, 10))

#Function to code with specific offset

new_message="""hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!
"""
def code(message, offset):
    result = []
    for x in message:
        ind = alphabet.find(x)
        if ind != -1:
            new_ind = ind - offset
            result.append(alphabet[new_ind])
        else:
            result.append(x)
    result = "".join(result)
    return result
print(code(new_message, 10))

#Brute Force Messgae with unknown offset

unk_message = """vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."""

for x in range(0,10):
    print(x)
    print(decode(unk_message, x))
    
 #The Vigenère Cipher
 #Decode
 
 v_message = """ dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp"""

def v_decoder(message, phrase):
    result = []
    new_phrase = []
    phrase_counter = 0
    for x in message:
        ind = alphabet.find(x)
        if ind != -1:
            new_phrase.append(phrase[phrase_counter])
            phrase_counter +=1
            if phrase_counter == len(phrase):
                phrase_counter = 0
        else:
            new_phrase.append(x)
            
        new_phrase_joined = "".join(new_phrase)
    
    for x in range(len(message)):
        ind_message = alphabet.find(message[x])
        ind_phrase = alphabet.find(new_phrase_joined[x])
        
        if ind_message != -1:
            new_ind = ind_message - ind_phrase
            result.append(alphabet[new_ind])
        else:
            result.append(message[x])
    result = "".join(result)
    return result
    
print(v_decoder(v_message, "friends"))

def v_coder(message, phrase):
    result = []
    new_phrase = []
    phrase_counter = 0
    for x in message:
        ind = alphabet.find(x)
        if ind != -1:
            new_phrase.append(phrase[phrase_counter])
            phrase_counter +=1
            if phrase_counter == len(phrase):
                phrase_counter = 0
        else:
            new_phrase.append(x)
            
        new_phrase_joined = "".join(new_phrase)
    
    for x in range(len(message)):
        ind_message = alphabet.find(message[x])
        ind_phrase = alphabet.find(new_phrase_joined[x])
        
        if ind_message != -1:
            new_ind = ind_message + ind_phrase
            result.append(alphabet[new_ind])
        else:
            result.append(message[x])
    result = "".join(result)
    return result
            


print(v_coder("you were able to decode this? nice work! you are becoming quite the expert at crytography", "friends"))
    
