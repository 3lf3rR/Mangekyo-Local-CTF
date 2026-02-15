<img width="555" height="736" alt="image" src="https://github.com/user-attachments/assets/db7386c2-bb3c-4ca0-b213-f959b6240286" />

# Challenge Name : Lost in The Melody 2.0
## Description :
The musician is back with a new track. This time, they whisper the secret not in the sound, but in the colors of silence. Close your eyes, open your eyes — but use the right ones.

"What can't be heard, might still be seen."

## Points : 160 pts
## File : `chall.wav`
## Difficulty : Easy

--------------------------------------------------
## Solution

- This challenge is nothing related to decoding an audio or anything , it's not morse , usual tools of steganography won't work , but remember the tool `audacity`; that i talked about in my workshop, let's use that
- Open the audio in audacity , you might say bro didin't find anything , yup you're right

<img width="1890" height="197" alt="image" src="https://github.com/user-attachments/assets/38bd5bb2-cc91-4734-be46-8e22ee84578f" />

- The description hints something interesting tho : "What can't be heard, might still be seen." , we can deduce that the flag is visual, hmmmm let's check somthing called spectogram of the audio ?!

----------------------------------------------------

### Spectogram ?

A spectrogram is a graph that displays the strength of a signal over time for a given frequency range. Using a color spectrum, it points to the frequencies where the signal’s energy is highest and shows the energy variation over time.

---------------------------------------------------

- You can view the spectogram of the audio by switching from `waveform to spectogram` when clicking on the three dots (...)

<img width="196" height="235" alt="image" src="https://github.com/user-attachments/assets/123a5216-4107-4961-a974-b0e4d005971d" />

<img width="1901" height="257" alt="image" src="https://github.com/user-attachments/assets/ef15818b-3277-472d-ab90-d6a46461493e" />

the flag is hidden in the spectogram :> , and you're done copy paste the flag , take your points :> !!

--------------------------------------------------------

### Flag : SecurinetsISTIC{t@7f0un4_lf4z4_ch9@wl3k}






