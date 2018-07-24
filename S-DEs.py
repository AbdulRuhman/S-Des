__author__="Mujahed Saleem"

key = "0111111101"

plain = "10100010"





P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)

P8 = (6, 3, 7, 4, 8, 5, 10, 9)

P4 = (2, 4, 3, 1)



IP = (2, 6, 3, 1, 4, 8, 5, 7)

IPi = (4, 1, 3, 5, 7, 2, 8, 6)



E = (4, 1, 2, 3, 2, 3, 4, 1)



S0 = [

        [1, 0, 3, 2],

        [3, 2, 1, 0],

        [0, 2, 1, 3],

        [3, 1, 3, 2]

     ]



S1 = [

        [0, 1, 2, 3],

        [2, 0, 1, 3],

        [3, 0, 1, 0],

        [2, 1, 0, 3]

     ]



def permutation(perm, key):

    permutated_key = ""

    for i in perm:
     
        permutated_key += key[i-1]

    

    return permutated_key




def F(right, subkey):

    expanded_plain = permutation(E, right)

    xor_plain = bin( int(expanded_plain, 2) ^ int(subkey, 2) )[2:].zfill(8)
    print(xor_plain)
    left_xor_plain = xor_plain[:4]

    right_xor_plain = xor_plain[4:]

    left_sbox_plain = Sbox(left_xor_plain, S0)

    right_sbox_plain = Sbox(right_xor_plain, S1)

    return permutation(P4, left_sbox_plain + right_sbox_plain)



def Sbox(input, sbox):

    row = int(input[0] + input[3], 2)

    column = int(input[1] + input[2], 2)

    return bin(sbox[row][column])[2:].zfill(4)



def fk(first_half, second_half, key):

     left = int(first_half, 2) ^ int(F(second_half, key), 2)

     print ("Fk: " + bin(left)[2:].zfill(4) + second_half)

     return bin(left)[2:].zfill(4), second_half



first_key = "01011111"

second_key = "11111100"



# this is inital  permutation for the plain text
permutated_plain = permutation(IP, plain)


# split the plain text into two 4bits 
first_half_plain = permutated_plain[:int(len(permutated_plain)/2)]

second_half_plain = permutated_plain[int(len(permutated_plain)/2):]




# estimate fk function according to the s-des algorithem 
left, right = fk(first_half_plain, second_half_plain, first_key)

print("SW: " + right + left)

left, right = fk(right, left, second_key) # switch left and right!



print ("IP^-1(Cipher): " + permutation(IPi, left + right))