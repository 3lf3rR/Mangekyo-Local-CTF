<img width="541" height="725" alt="image" src="https://github.com/user-attachments/assets/a4e47cac-acf6-47a1-9151-b6fa6528aa22" />

# Challenge Name : Lost in the Traffic
## Points : 400 pts
## Difficulty : Hard
## File : `challenge.pcap`

----------------------------------------

<img width="1910" height="543" alt="image" src="https://github.com/user-attachments/assets/fa139243-b42c-4e7a-a1a6-b3f673e6fc0d" />

- if you filter and see the http packets you'll see random **GET** requests to fake site, but that's not what we want. On the other hand if you check the POST requests using this query

```bash
http.request.method == POST
```

<img width="1363" height="520" alt="image" src="https://github.com/user-attachments/assets/ad5a6863-83ac-46f1-826f-37c231e7e129" />

- You'll probably say bro there is nothing but if we hit follow `tcp stream` on these **POST request** , you'll see that each packet has a caracter of our flag reassemble them to get your flag

<img width="786" height="272" alt="image" src="https://github.com/user-attachments/assets/d4973e6b-0f23-4e61-a025-88c7a15b87cb" />

- After reassembling the caracters, you'll get

```bash
SecurinetsISTIC{P0ST_r3qu35T_chunks}
```

And You're Done :> !!

-------------------------------------------------

### Flag : SecurinetsISTIC{P0ST_r3qu35T_chunks}






