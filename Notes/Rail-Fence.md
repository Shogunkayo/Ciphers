# RAIL-FENCE CIPHER
---
- Easy to crack transposition cipher which follows a simple rule for mixing up characters 
- Offers no communication security
- Difficult to break when combined with substitution cipher
- The key is the number of "rails"
- "write down the columns, read along the rows"

for the plaintext,
`defend the east wall of the castle`

ciphertext is `dnetlhseedheswloteateftaafcl`
```
d . . . n . . . e . . . t . . . l . . . h . . . s . . .
. e . e . d . h . e . s . w . l . o . t . e . a . t . e
. . f . . . t . . . a . . . a . . . f . . . c . . . l .
```
for key = 3

ciphertext is `dttfsedhswotatfneaalhcleelee`
```
d . . . . . t . . . . . t . . . . . f . . . . . s . . .
. e . . . d . h . . . s . w . . . o . t . . . a . t . .
. . f . n . . . e . a . . . a . l . . . h . c . . . l .
. . . e . . . . . e . . . . . l . . . . . e . . . . . e
```
for key = 4

