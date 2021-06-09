#length(string) function
kahani= "once there was a"
print(len(kahani))                #lenth is 16 including the space,count!


#string.endswith("word") function
print(kahani.endswith("w"))       #it prints true/false. I serached if string 'Kahani'
                                  #ends with word/element "a"..which it's. So,it's TRUE.


#string.count("word") fuction
print(kahani.count("e"))         #counts how many times the element repeats.
                                 #'e' 3 times in this string.

#string.find("word") function
print(kahani.find("there"))      # find the first occarence of the word 
                                 # which index of string. here it's '5' where's 'there'. Note: if the index can't be found then output shows "-1"

#string.capitalize() fuc
print(kahani.capitalize())      #auto capitalization of the starting word of sentence.

#string.replace("old element","new element")
print(kahani.replace("a","baal"))  #replace all existing string elements by a new given element upon old element.
                                   #ex: here all 'a' will be replaced.So, prints 'once there wbaals baal'



#escape sequence characters: \n  ,  \t  , \ or, \\  (new line, a space tab, single oblique prints both)
story="bla bla black sheep\tseat on a owl\tyes sir sir."
story1="bla bla black \t       sheep seat on a owl\nyes sir sir."
story2="bla bla black sheep\nseat on a owl\\yes sir sir."
print(story)
print(story1)
print(story2)