n = int(input(""))
faces = 0
while n > 0: 
    n-=1    
    str = input("")

    if str == "Tetrahedron":
        faces+=4
        continue
    elif str == "Dodecahedron":
        faces+=12
        continue
    elif str == "Cube":
        faces+=6
        continue
    elif str == "Octahedron":
        faces+=8
        continue
    elif str == "Icosahedron":
        faces+=20
        continue
    else:
        break
    

print(faces)
    
