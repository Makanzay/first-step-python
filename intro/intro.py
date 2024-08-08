
#introduction to python developement 
#initiation 
print("hello world")

#python interpreter is a calculator 
print(3+7)
print(4*8)
print(15/3*2)

#save data into variable 
age = 18 
age1 = 20
print(f'age = {age} et age 2 = {age1}')

#different variable type 
a = 6 #integer
b= 6.5 #floating point
c="love" #string
d=["lol",53,6.3] #array
e= True #boolean
d=('no',45)# same as array but immutable
print(a,b,c,d,e,d)

#array maniputlation usefull
plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]

print(plateformes_sociales[0])
#element with array are mutable with the indice #
#and you can add item with append() delete with remove()
plateformes_sociales.append("tiktok")
print(plateformes_sociales)
#access to item the same way for the string value
text = "python"
print(text[2])#the letter t 
print(len(text)) #length of a str or array

#you car sort an array with .sort()

#complexe data dictionnary 

taux_conversion = {}
taux_conversion['facebook']=3.4
taux_conversion['instagram']=1.2

print(f'the dictionnary is {taux_conversion}')
#and the name is the indice of this complex array
#del taux convertion [indice] way to delete a pair

#Flow control with the If n Else n Elif 

if age >= 18 :
    print('he is an adult')
elif age < 0:
    print('you doesn t exist ')
else:
    print('you are minor')

#there is condition booleen op and  or not 
#the operator of comparaisoon 

#to evoid a too big if elif combination 
#there is the match case :

fruit='pomme'
match fruit:
    case"pomme":
        print('j aime les pommes')
    case "banane":
        print('j aime les bananes')
    #possible to add to infini
    case _:#the end case don t forget the space before the underscore
        print('i don t know this fruit')

#repeat task include the loop and ellse
