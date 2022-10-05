# ATBASH CIPHER
---
- Substitution cipher where letters of alphabets are reversed 
- Originally used for the hebrew alphabet
- Offers no security and can be broken easily 
- It is also an Affine Cipher with a=25 and b=25

Substitution key
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ZYXWVUTSRQPONMLKJIHGFEDCBA
```

pycipher module
```
pycipher.Atbash().encipher("message")
pycipher.Atbash().decipher("message")
```