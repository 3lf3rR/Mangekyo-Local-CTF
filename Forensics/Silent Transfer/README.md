<img width="600" height="793" alt="image" src="https://github.com/user-attachments/assets/d8d39d68-f6d6-4c68-b5f1-3a8246a6ae39" />

# Challenge Name : Silent Transfer
## Difficulty : Medium
## File : `Chall.pcap`

----------------------------------

- If we explore more this network capture and if we read carefully the decription it says **"data was quietly retrieved"** and we have hints on the title that says **"Transfer"** , so we have a data that was stolen and this data could be credentials to something for this we need to see the **protocols** we have on this network capture
, if we go to `Statistics > Protocol Hierarchy` we can see all the protocols we have

<img width="1276" height="240" alt="image" src="https://github.com/user-attachments/assets/c6d6e895-2874-40a8-9d21-6df9c6fc2c41" />

- Let's investigate more on the `FTP` Protocol which is a protocol used for **transfering files** , let's use this query on `wireshark`

```bash
FTP
```

<img width="1221" height="386" alt="image" src="https://github.com/user-attachments/assets/9811c7e2-ed24-4b46-98f9-1ea325ca1e74" />

- Let's look for `Login Successful` Packets to grab username and password used to log in

<img width="1147" height="246" alt="image" src="https://github.com/user-attachments/assets/bb7d87d8-b0ba-45e8-bdb5-b418c47489cb" />

And you're done :>

------------------------------------------

### Credentials : `admin:ftp123`

### Flag : SecurinetsISTIC{admin,ftp123}


