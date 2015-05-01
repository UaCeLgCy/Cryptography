import string 
from random import *
import os
import time

debut = time.clock()
print ("▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄ ▲ ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄▼ ◄ ▲ ► ▼ ◄ ▲ ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄ ▲ ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄▼ ◄ ▲ ► ▼ ◄ ▲ ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄ ▲ ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄▼ ◄ ▲ ► ▼ ◄ ▲ ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄ ▲ ▼ ◄ ▲ ► ▼ ◄ ▲ ► ▼ ◄ ▼ ◄ ▲ Sorry, dropped my bag of illuminati")




def generation_clef(a,b):
    clef = ''
    i = 0

    if a == 1:
      for i in range(int(b)):
          n = randrange(0,26) #génére un nombre aléatoire entre [1;27[

          lettreClef = chaine[n] #vas chercher la lettre correspondant dans la chaine 1

          clef += chaine[n] #pose la lettre dans la chaine clef

          i = i + 1

          
    elif a == 2:

         while i < int(b):
            n = randrange(0,53) #génére un nombre aléatoire entre [1;53[

            lettreClef = chaine[n] #vas chercher la lettre correspondant dans la chaine 1

            clef += chaine[n] #pose la lettre dans la chaine clef

            i = i + 1  

    elif a == 3:
        
        while i < int(b):
            
            n = randrange(0,80) #génére un nombre aléatoire entre [1;81[

            lettreClef = chaine[n]

            clef += chaine[n] #pose la lettre dans la chaine clef

            i = i + 1

            

        a = 0  


    else:
        fin = time.clock()
        print("ntm, pas de temps a perdre. Tu ma deja fait perdre",(fin - debut)* 10,"secondes")

    print(clef)



print("Welcome")
b = input("entrez la longeur de la clef : ")
a = float(input("entrez la complexitée de la clef (1=simple,2=moyen,3=complexe) : "))


chaine = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN&É-_ÇÀ=$*Ù!;:,><&é,;!èù*$=àç"
chaine = str(chaine)

generation_clef(a,b)



fin2 = time.clock()


print("généré en ",(fin2 - debut)* 10,"secondes")


print("   ================================= FIN =================================")



            
             
