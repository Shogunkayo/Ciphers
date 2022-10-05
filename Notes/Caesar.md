# CAESAR CIPHER
----
- One of the earliest substitution ciphers
- Each alphabet is shifted a certain number of places
- Requires a key to encrypt and decrypt which specifies the shift

Mathematical Description
```
e(x) = (x+k) mod(26)
d(x) = (x-k) mod(26)
```

pycipher module
```
pycipher.Caesar(key=k).encipher(message)
pycipher.Caesar(key=k).decipher(message)
```

### Cryptanalysis
- As the shift has to be a number between 1 and 25, brute force to get a readable text is possible
- If brute force doesnt, work we can try analysising the number of times a certain alphabet repeats 
- The below graph shows the frequency of letters of the English alphabet![[letter_frequencies_2.png]]