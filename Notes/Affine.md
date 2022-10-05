# AFFINE CIPHER
---
- less secure than a substitution cipher as other attacks in addition to ones targeted to a substitution cipher, may work
- If the plaintext of two ciphertext characters are found, then the key can be obtained by solving a simultaneous equation

### Algorithm
- Key consists of two numbers `a` and `b` 
- For a 26 letter alphabet set `m = 26`
- `a` should be relatively prime to `m`
- `p` is the number representing the letter

ciphertext `c = ap + b mod(m)`

decryption function `p = a'(c-b) mod(m)`
where `a'` is the multiplicative inverse 

- Let `x` be the multiplicative inverse, `ax = 1 mod(m)`
- Substituting each number is the easiest way to solve the above equation

-> `m` need not be 26, it represents the total number of characters in the alphabet set (digits, punctuation, uppercase letters can be added)

pycipher module
```
pycipher.Affine(a=5,b=9).encipher(message)
pycipher.Affine(a=5,b=9).decipher(message)
```

### Cryptanalysis
- Cipher is easy to break when `c` and `p` are known for two values
- To obtain `a` and `b`, find `D = p0-p1` and `D'`
```
a = D'(c0 - c1) mod(m)
b = D'(p0c1 - p1c0) mod(m)
```