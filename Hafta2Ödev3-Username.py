##anahtar=1
##rakam=0
##while True:
##
##    while anahtar==1:
##        username=input("Please write your username with 3-18 characters")
##        number="0123456789"
##        for i in username:
##            if i in number:
##                rakam += 1            
##
##        if rakam != 0 :
##            print("Numbers can not be added in username. Please try again")
##            
##            continue
##        elif 3 > len(username) or len(username) >18:
##            print("Your username must be in 3 and 18 characters")
##        
##
##        else:
##            print("Your username:",username)
##            anahtar=2          
##
##    while anahtar ==2:
##        password=input("Please write your password with 6-12 characters")        
##        if len(password)<=6 or len(password)>=12:
##            print("Please write your password with 6-12 characters")
##        else:
##            print("Your password:",password)
##            break
##    break
##dosya=open("usernamePassword.txt","w")
##print(
##"Username:",username,
##"Password:",password,sep="\n",file=dosya)
##dosya.close()

##anahtar=1
##rakam=0
##while True:
##
##    while anahtar==1:
##        username=input("Please write your username with 3-18 characters")
##        number="0123456789"
##        if 3 >= len(username) or len(username) >=18:
##            print("Your username must be in 3 and 18 characters")
##            continue
##        for i in username:
##            if i in number:
##                rakam += 1            
##
##        if rakam != 0 :
##            print("Numbers can not be added in username. Please try again")
##            
##            continue
##        
##        else:
##            print("Your username:",username)
##            anahtar=2          
##
##    while anahtar ==2:
##        password=input("Please write your password with 6-12 characters")        
##        if len(password)<=6 or len(password)>=12:
##            print("Please write your password with 6-12 characters")
##        else:
##            print("Your password:",password)
##            break
##    break
##dosya=open("usernamePassword.txt","w")
##print(
##"Username:",username,
##"Password:",password,sep="\n",file=dosya)
##dosya.close()

anahtar=1
rakam=0
while True:

    while anahtar==1:
        username=input("Please write your username with 3-18 characters")
        number="0123456789"
        if 3 >= len(username) or len(username) >=18:
            print("Your username must be in 3 and 18 characters")
            continue
        for i in username:
            if i in number:
                rakam += 1            

        if rakam != 0 :
            print("Numbers can not be added in username. Please try again")
            
            continue
        
        else:
            print("Your username:",username)
            anahtar=2          

    while anahtar ==2:
        password=input("Please write your password with 6-12 characters")        
        if len(password)<=6 or len(password)>=12:
            print("Please write your password with 6-12 characters")
        else:
            print("Your password:",password)
            break
    break
dosya=open("usernamePassword.txt","w")
print(
"Username:",username,
"Password:",password,sep="\n",file=dosya)
dosya.close()
