

letter='''Dear <|x|>,\nGund marao. Appni bhi,apka dost ko bhi
Date: <|y|> '''          #<||> captures the word.we can't use string.repace(old,new) function directly here.

nam=input("Name:\n")
samay=input("Date: ")
letter=letter.replace("<|x|>", nam)  #letter=letter.replace() means,  in first 'letter' final output will be
                                    #COPIED (note:new variable can't be taken intead of 'letter'/ keep it same variable as this program taking input..)
                                   #from second "letter.replace()" input [both variable should be same for the copy or, easiness u can say like (letter=letter....)]      
letter=letter.replace("<|y|>", samay)  #and in second "letter.replace()" , is where replacement happen from the input.
print(letter)