<img width="533" height="735" alt="image" src="https://github.com/user-attachments/assets/e7e9e561-9c79-4923-9af9-a57707ecfed4" />

# Challenge Name : Lost in the Melody 3.0
## Points : 200
## File : `chall.wav`
## Description : 

Ever hear a dial-up modem singing in the void? This audio clip contains a sequence… a call waiting to be answered. The tones speak numbers, and numbers speak secrets.

***“Listen to the phone’s old song — it knows the combination.”***

---------------------------------------------------------

- If you open the file and listen you 'll know that's a **DTMF Tone**

### DTMF Tone

DTMF (Dual-Tone Multi-Frequency) tones are commonly used in CTF (Capture The Flag) challenges, especially in forensic and steganography categories.  These tones are the sounds produced when pressing keys on a traditional telephone keypad, each consisting of two simultaneous frequencies.

- there is an online tool that will make our lifes easier

**Online Tool :** [DTMF Decoder](https://dtmf.netlify.app/)

<img width="982" height="211" alt="image" src="https://github.com/user-attachments/assets/255e74cb-beaf-4d4e-bda7-47ec079e9e2c" />

- Then scroll down to see the output

```bash
Decoded: 83 101 99 117 114 105 110 101 116 115 73 83 84 73 67 123 52 117 100 49 48 95 100 116 109 102 95 53 48 85 110 100 125
```

- You're not done yet remember the **flag format** (SecurinetsISTIC{...}) ?! , we can see that `83` if we decode from **ascii** to **plain text** we get the caracter `'S'`

<img width="910" height="213" alt="image" src="https://github.com/user-attachments/assets/52c209a4-eaca-4c18-a419-d671fb9f03d0" />

That's it see it's easy :> !! 

-----------------------------------------------------------

### Flag : SecurinetsISTIC{4ud10_dtmf_50Und}









