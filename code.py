shift = 5
eSentence = input("Please enter a sentence: ")
encryption = ""
for ch in eSentence:
        if ch.isalpha():
            position = ord(ch)
            positionIndex = position - ord('a')
            newIndex = (positionIndex + shift) % 26 
            newText = newIndex + ord('a')
            newChar = chr(newText) 
            encryption = encryption + newChar
print("The printed sentence is: ", encryption)
