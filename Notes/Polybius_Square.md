# POLYBIUS SQUARE CIPHER
---
- Simple substitution cipher where each plaintext character is enciphered as 2 ciphertext characters
- Can be detected if there are only around 5-6 characters in the ciphertext

### Algorithm
- Keys usually contain a 25 letter "key square"
```
   A B C D E
A| p h q g m
B| e a y l n
C| o f d x k
D| r c v s z
E| w b u t i
```

```
d e f e n d  e a s t  w a l l  o f  t h e  c a s t l e 
CCBACBBABECC BABBDDED EABBBDBD CACB EDABBA DBBBDDEDBDBA
```

- ADFGVX cipher uses 6x6 version of polybius square in the first stage of its encryption

pycipher module
```
p = PolybiusSquare('phqgiumeaylnofdxkrcvstzwb',5,'ABCDE')
p.encipher('plaintext')
p.decipher('ciphertext')
```