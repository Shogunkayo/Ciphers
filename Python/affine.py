import sys

def encipher(a, b, m, plaintext, key):
    ciphertext = []
    
    for i in plaintext:
        if(i!=' '):
            ciphertext.append(key[(a*key.index(i) + b)%m])
    return "".join(ciphertext)

def decipher(c0, c1, p0, p1, m, ciphertext, key):
    c0 = key.index(c0)
    c1 = key.index(c1)
    p0 = key.index(p0)
    p1 = key.index(p1)

    d = p0-p1
    for d_inv in range(m):
        if(d_inv*d % 26 == 1 ):
            break
    
    a = (d_inv *(c0-c1))%m;
    b = (d_inv*(p0*c1 - p1*c0))%m;

    for a_inv in range(m):
        if(a_inv*a % 26 == 1 ):
            break

    return "".join([key[(a_inv*(key.index(ciphertext[i])-b))%m] for i in range(len(ciphertext))])
  
##------------------CHANGE ALPHABET SET HERE-----------------------

alphabet_set = list("abcdefghijklmnopqrstuvwxyz")

##-----------------------------------------------------------------

try:
    if(sys.argv[1] == 'e'):
        plaintext = input("Enter string: ")
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        for i in range(2,len(alphabet_set)):
            if(a%i==0 and len(alphabet_set)%i==0):
                print("'A' SHOULD BE COPRIME TO LENGTH OF THE ALPHABET SET")
                sys.exit()


        print(encipher(a,b,len(alphabet_set), plaintext, alphabet_set))

    elif(sys.argv[1] == 'd'):
        ciphertext = input("Enter enciphered text: ")
        ans = int(input("How many pairs are known?: "))
        if(ans == 0):
            print("Too many possible keys")
        elif(ans == 1):
            c0, p0 = input("Enter ciphertext, plaintext value pair: ").split()
            with open("deciphered.txt", 'a') as file:
                for c1 in alphabet_set:
                    for p1 in alphabet_set:
                        file.write(decipher(c0, c1, p0, p1, len(alphabet_set),ciphertext, alphabet_set)+"\n")
        else:
            c0, p0, c1, p1 = input("Enter ciphertext, plaintext value pairs: ").split()
            print(decipher(c0, c1, p0, p1, len(alphabet_set), ciphertext, alphabet_set))

except:
    print("COMMAND LINE ARGUEMENTS-")
    print("e : perform encryption")
    print("d : perform decryption")
    print("Default alphabet set is from lowercase a to lowercase z")
