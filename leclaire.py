import string 

# defintion of the function that codes message 'c' with key 'k'
def crypt(c, k):
    V = string.ascii_letters 	# V contains all characters (capital and noncapital letters)
    N = '' 	# defintion of a empty string
    for i in c: 	# for each letters 'i' in the message 'c'
        if i in V: 	# check if 'i' belongs 'V' 
            p = V.index(i)	# 'p' contains index of 'i' in 'V'
            if p < 26 :		# Check 'i' is noncapital letters
                N += (V[(p+k)%26])	# add the letters number '(p+k)%26 of 'V' at string 'N'. '%26' for (p+k)>len(V)
            else:
                N += (V[(p+k)%26+26]) 	# '+26' because the capital letters start at index 26 in 'V' (p+k)>len(V)
        else:
            N += i 	# add 'i' not belongs in 'V'
    return N
