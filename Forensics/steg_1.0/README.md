<img width="1645" height="395" alt="image" src="https://github.com/user-attachments/assets/f2f28ebc-e752-46ab-bc54-61a0f7db4c43" /><img width="565" height="573" alt="image" src="https://github.com/user-attachments/assets/f2acc988-a27e-42c3-9173-b540ee6a4dc8" />

# Challenge Name : Steg 1.0
## Difficulty : Easy
## File : `flag.jpeg`

--------------------------------------------------
- This is a basic image steganography challenge solvable with the famous steg tool `steghide`, but as we all know this tool need a passphrase to extract hidden data in images, for this we will first the **metadata** of the image more likely tha passphrase is hidden there.

<img width="1458" height="633" alt="image" src="https://github.com/user-attachments/assets/8b79fc3c-25f3-4fef-a1b7-d2ded7825234" />

```bash
Passphrase : Sup3rDup3rrp4ssw0rD9933684
```
- Let's now uncover the hidden data using `steghide`

```bash
steghide extract -sf flag.jpeg
```

`extract` : Tells Steghide to extract hidden data from a carrier file.

`-sf` : Specifies the file that contains hidden data.

`flag.jpeg` : Our Image that contains the hidden data.

<img width="1645" height="395" alt="image" src="https://github.com/user-attachments/assets/415b807f-9d0d-4b1f-8d18-60836fb5b944" />

And you're Done :> , see EASSSSSYYYYY!!!

----------------------------------------------------

### Flag : SecurinetsISTIC{w3ll_d0n3_5t3g4n0gr4phy_1sFUN}
