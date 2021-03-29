import re

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

findWholeWord('seek')('those who seek shall find')    # -> <match object>
findWholeWord('word')('swordsmith')
string = "Hello my friends I'm here to talk about the future technology in our universal existence"
possible_answers = ['Yes', 'yes', 'Alright', 'alright', 'Ok', 'OK', 'ok', 'O.K.', 'o.k.', 'O.k.']
if findWholeWord('Technology')(string):
    print('logy')
else:
    print("why not")

print("Welcome to the Party Friend!")
Emotional_state = input("How are You Today?:")
Positive_Emotion = ["good", "fine", "happy"]
if any( [emotion in Emotional_state for emotion in Positive_Emotion] ):
    print("That's Great! Happy to have you here!")