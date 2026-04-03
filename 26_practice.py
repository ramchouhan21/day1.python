# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
fav_lang = {}
a = input("enter the name of friend1:")
fav_lang[a] = input("enter the fav lang of friend1:")
b = input("enter the name of friend2:")
fav_lang[b] = input("enter the fav lang of friend2:")    
c = input("enter the name of friend3:")
fav_lang[c] = input("enter the fav lang of friend3:")
d = input("enter the name of friend4:")
fav_lang[d] = input("enter the fav lang of friend4:")
print(fav_lang)