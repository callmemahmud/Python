a = 'baal'                    #it's obvious
print(a)

a="baal's"                   #we can use single quote within double quote 
print(a)

a='''baal'd a rockstar fren. he liked   
to seat on "rock".
'''                          #within triple quote all can be witten.
print(a)

b= 'YOU KNOW, '
print(b+a)                   #we can add two word like this.


#searching 
r='PUNK'
print(r[1])      # we can search elements through print( variable  [the number of element] 
                 # but we can't change element in strings like this.Ex: c[1]=A, it won't work in pyhton.


#string slicing
print(r[0:3])    #it prints from element of [0] to right BEFORE element of [3],which is [2]
print(r[1:4])    #prints 'UNK' as element[1] to before element[4]
 
print(r[0:])     #noting in right means,there's auto the highest PRINTABLE element, here it's [4] or,[0:4]
print(r[:3])     #nothing in left side means, there's auto [0], as the lowest it is.


#in string elements is starts with [0]..but in in negative elment consideraiton,it menas highest negative(negative of length, here 4 words) length will
#take place on [0]. ex: PUNK= will be counting as -4=[0],-3=[1],-2=[2],-1=[3]..   notice: there's no '0' in negative,mind it.

print(r[-4:-2])    #it means -4 to before of -2 or, -3=[1] . It prints 'PU'




#string slicing with skip
d="draftpunk"

o=d[1:8:2]    #formation: [startng element: print till highest element: skip after print each time(it also refers previous element )]
print(o)      #ex:here [1:8] will be printed which's, 'raftpunk' but [1:8:2] menas it'll skip next 1 element(skiping will be the previous number of given value,here 1 word skip), each time it prints. 
            # so, it'll print 'rfpn' in final.
#it's  better to take extra variable(here,o) for this formation to print.

e=d[0::2]    #remenber! left side nothing means highest printable element, here[0:9]

print(e)   #prints [0:9] which is 'draftpunk' , [0:9:2] means 1 word skip after print;
           #which's 'datuk' .


