<img width="591" height="786" alt="image" src="https://github.com/user-attachments/assets/9aa83059-c46f-4b7f-9dbd-bd8079ef35c8" />

# Challenge Name : Introduction To Wireshark
## Tools Needed : `Wireshark`
## File Provided : `Challenge.pcap`
-------------------------------------------------------
## What is `Wireshark` ?

Wireshark is the world’s most popular network protocol analyzer — a free, open-source tool that captures and analyzes network traffic in real time. Whether you’re an IT professional troubleshooting connectivity issues, a cybersecurity analyst hunting for threats, or a developer optimizing microservices, Wireshark is an indispensable tool in your arsenal.

Available on Linux, macOS, and Windows, Wireshark supports multiple protocols including HTTP, TCP, UDP, DNS, and hundreds more. It transforms raw network packets into structured, readable data that helps you understand exactly what’s happening on your network.

-------------------------------------------------------
## Solution
- Open `Wireshark` and explore the Network Capture

<img width="1918" height="620" alt="image" src="https://github.com/user-attachments/assets/75dbecaf-419a-4246-be15-915cc160c1f0" />

- As you can see a lot of `TCP Packets` if we dig more we find something interesting appears like our flag chunks

<img width="1817" height="561" alt="image" src="https://github.com/user-attachments/assets/daa10eb1-9ef8-4c83-a7ac-c76d0adaf406" />

- If we assemble them into one string we get
```bash
SecurinetsISTIC{TCP_Reassembly_Win}
```

And That concludes it we have our Flag , You're Done :>

### Flag : SecurinetsISTIC{TCP_Reassembly_Win}

 
