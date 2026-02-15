<img width="575" height="583" alt="image" src="https://github.com/user-attachments/assets/e9d5a666-3e6d-4f08-973a-984c67104b8f" />

# Challenge Name : Hidden in Text 2.0
## Description : 
We have intercepted a suspicious text file that appears normal at first glance, but we believe it contains hidden data. Analyze the file carefully to uncover what's hidden inside.
## Points : 175 pts
## Difficulty : Easy
## File : `Chall.txt`

--------------------------------------------

## Solution
- ok first i need you to notice something , open the file `.txt` in notepad

<img width="1255" height="377" alt="image" src="https://github.com/user-attachments/assets/6d6945a0-f99b-4454-92bb-ab216ff50201" />

- I want to introduce something new to you :> ➡️ **Zero Width Steganography**

-----------------------------------------------

### Zero Width Steganography ?

**Zero-width steganography** is a technique that **hides secret messages within plain text** using **invisible Unicode characters** with zero width, such as U+200B (Zero Width Space), U+200C (Zero Width Non-Joiner), and U+200D (Zero Width Joiner). 

---------------------------------------------------------
- Back to it to decode the hidden text , and unvail the hidden unicode caracters we can use an online zero width steganography tool

**Tool :** [StegZero](https://stegzero.com/)

<img width="1225" height="677" alt="image" src="https://github.com/user-attachments/assets/f7045841-d37c-465c-9ef3-27eec68fe9ec" />

There you go , easy right :> !!

-----------------------------------------------------------

### Flag : SecurinetsISTIC{z3r0_w1dth_5t3g4n0gr4phy}




