<img width="542" height="576" alt="image" src="https://github.com/user-attachments/assets/c56b242c-cca2-400b-97f0-50046e2d1d61" />

# Challenge Name : Steg 2.0
## File : `chall.png`

## Solution

- Sorry but in this task neither `steghide` nor `zsteg` or that shit work :> , we're gonna use python based tool called `stepic`

### Stepic
- Stepic provides a Python module and a command-line interface to hide arbitrary data within images. It slightly modifies the colours of the pixels in the image to store the data.
- install :
```bash
pip install stepic
```

- now to grab the hidden flag type this command
```bash
stepic -d -i chall.png
```

`-d` : decode

`-i` : where you input your image 

<img width="913" height="113" alt="image" src="https://github.com/user-attachments/assets/6dcd0e97-559b-4bb8-ad17-d4a3fc4b2b94" />

And you're Done <3

### Flag : SecurinetsISTIC{h1dd3n_1n_p1X3l5_9635@}
