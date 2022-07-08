#Project1

# First Part ##############################################################


liste = []
liste1 = [1,2,3,[4,"dog",5,6,[7,8,9,10],11],12,[13,14],15]
for i in liste1 :
    if(type(i)==list):
        for j in i:
            if(type(j)==list):
                for k in j :
                    if(type(k)==list):
                        
                        for p in k :
                            liste.append(p)
                    else:
                        liste.append(k)
            else: 
                liste.append(j)
    else:
        liste.append(i)


print(liste)



# Second Part ##############################################################

print("*************")
liste2 = [1,2,3,[4,"dog",5,6],[7,8,9,10],11,12,[13,14],15]
liste2 = liste2[::-1]
for i in liste2 :
    if(type(i)==list):
        a = i[::-1]
        q = liste2.index(i)
        liste2[q] = a
        
print(liste2)