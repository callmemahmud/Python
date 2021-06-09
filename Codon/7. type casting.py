a= "1234"
#print(a+5) <--we cant add rn as, the inverted is string type

a= int(a)    #notice: we've taken "a" as variable again, tho previously it was 'a'=1234 ; we could take
                                 #b  [like, b=int(a), and print (b+5) ]..just to show in python we can use same variable again.
print("a + five:", a+5)
#but mix func type can't be happened like a=12abc34 or, 123.6768. 



a= float(a)                        #look, again we used 'a' [a= f...], same variable.
print("   as floating =", a)

a= str(a)                      #again, same variable[a= st..]
print("by string: ", a)            #look, in this line ( 'a' was floating in previous output),
                                   #by a= str(a)  {could be written as [ x=str(a),print(x) ] i mean with diff variable}; it converts previous float(a) into str(a);
                                   #thus,float can be converted into string.Basically here string been converted based on previous output as in it's just random word.

#if you don't believe, then
print(type(a))  #see!