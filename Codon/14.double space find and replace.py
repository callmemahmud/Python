m="hi  what's  is    up?"
x= m.find("  ")          #remember, [string.find("word")] func? , here we use diff variable cause no input yet.
print(x)                 #prints the index of string where is double space, here's [2]..so 2 will be printed.
                         #if there's no double space it'll print -1



#replace the double space with single space
x=m.replace("  "," ")        #remember, [string.replace("old","new")] func?
print(x)                     #prints all the doublespace into single space.But if there're two double space in string (like here before "up") then it'll 
                             #convert into a single double space..we'll solve it more efficiently in Loop.

