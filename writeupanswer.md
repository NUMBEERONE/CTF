### https://ctf.cyber-cit.club/challenges

# 🏁 CTF@CIT 2026 – Writeups

This repository contains structured solutions for CTF@CIT 2026 challenges across multiple categories.

---

# 🌐 Web Category

## A Massive Problem
- Intercept account creation request (Burp Suite)
- Add `"role": "admin"` in JSON body
- Gain admin access

**Flag:** `CIT{M@ss_@ssignm3nt_Pr1v3sc}`

---

## Debug Disaster
- Directory brute force (`dirsearch`)
- Find `/admin/flg_bar`

**Flag:** `CIT{H1dd3n_D1r5_3v3rywh3r3}`

---

## Intern Portal
- Notice `?id=` parameter
- Use Burp Intruder (0–500)
- Filter by Content-Length → ID 347

**Flag:** `CIT{Acc355_C0ntr0l_M@tt3rs!}`

---

## Server Components
- Identify React2Shell vulnerability
- Use RSC-Security-Analyzer
- Read `/opt/flag.txt`

**Flag:** `CIT{R3aCt_1s_Vu1n3r@bl3}`

---

## Hit Your Limit
- Rate-limited API
- Use multithreaded brute-force script

**Flag:** `CIT{R@T3_L1m1t1nG_15_Bypass@ble}`

---

## Temporary Destruction
- SSTI confirmed with `{{7*7}}`
- Bypass filters (`__globals__`)
- Read `/tmp/flag.txt`

**Flag:** `CIT{55T1_R3m0t3_C0d3_3x3cut1on}`

---

## Sign Up and Enjoy
- Flask cookie (not JWT)
- Crack secret using `flask-unsign`
- Secret: `Password1!`
- Forge admin cookie

**Flag:** `CIT{W3ak_S3cr3t5_C@n_B3_Un5ign3d}`

---

# 🧩 Misc Category

## SAM, I am
- Crack MD5 hash via CrackStation

**Flag:** `CIT{C1t!!}`

---

## Robots
- Check `/robots.txt`

**Flag:** `CIT{S8kMc789Gd37Py1gQPiWbeqxx}`

---

## Call me, maybe?
- Crack bcrypt hash using hashcat

**Flag:** `CIT{8675309jenny}`

---

## Dog barking
- Decode frequency → binary → ASCII

**Flag:** `CIT{b4rking_up_th3_wr0ng_tr33}`

---

## What’s the word?
- Office file → extract hash → crack password

**Flag:** `CIT{b1rd_1s_th3_w0rd}`

---

# 🎮 Game Category

## Coin Jam
- Modify memory using Cheat Engine
- Change coins 7 → 10

**Flag:** `CIT{5x4W28cLIbUq}`

---

# 🔐 Crypto Category

## Brainiac
- Brainfuck interpreter

**Flag:** `CIT{Wh@t_in_th3_w0rld_i$_th1s_l@ngu@g3}`

---

## The Onion
- Multi-layer Base64 decoding
- Crack MD5 hash

**Flag:** `CIT{iloveharrypottersomuchthaticouldreadallthebooksintwodaysmostlikely}`

---

## Baby Exponent
- RSA small exponent attack (e = 3)

**Flag:** `CIT{sm4ll_3xp0n3nt_g0_brrr}`

---

## Rotor Rooter
- Enigma cipher decoding

**Flag:** `CIT{we_can_only_see_a_short_distance_ahead_but_we_can_see_plenty_there_that_needs_to_be_done}`

---

# 🖼️ Steganography Category

## Hidden Image Challenge
- Check metadata

**Flag:** `CIT{ur_w4rm1ng_up_n0w}`

---

## Are ya winning, son?
- Hex editor manipulation of JPEG height bytes

**Flag:** `CIT{pls_d0nt_b3_l1k3_th1s_guy}`

---

## Cool Car
- StegSolve Alpha plane 0 → Base64 decode

**Flag:** `CIT{4Vu1u1zh}`

---

## There’s no room left
- Zero-width character decoding
- Map to binary → UTF-16

**Flag:** `CIT{ok_maybe_not_plain_sight}`

---

## Car Crash
- XOR image layers
- Decode Base64

**Flag:** `CIT{7E3qU4wE}`

---

# 🔍 Forensics Category

## The Evil Files
- Extract hidden PDF metadata (CC field)

**Flag:** `CIT{m0j0_eng4g3d}`

---

## Larping 101
- Extract PPT with binwalk
- Find XML flag

**Flag:** `CIT{l4rp_l4rp_l4rp_s4hur}`

---

## The click that may have fixed
- PowerShell history analysis
- Browser SQLite history extraction

**Flag:** `CIT{2026-04-18T07:07:26Z}`

---

## Wiretap
- Decode modem audio using minimodem

**Flag:** `CIT{g3t_0ff_th3_ph0n3_1m_0n_th3_1ntern3t}`

---

# ⚙️ Reverse Engineering Category

## Catacombs
- `strings` + grep

**Flag:** `CIT{3R2rA2J0PdFH}`

---

## Say My Name
- `strings` + grep

**Flag:** `CIT{Zn583Umnwd4S}`

---

# 🚀 Fullpwn Category

## Goober 1
- FTP access (guest:guest)
- Crack KeePass database
- Extract credentials

**Flag:** `CIT{ftp_d33z_nut$}`

---

## Goober 2
- SSH access
- `.bash_history` enumeration
- Symlink trick to bypass permissions

**Flag:** `CIT{Br41n_bLa$t3R}`

---

# 🕵️ OSINT Category

## Yannella
- Search identity + affiliation

**Flag:** `CIT{US_Department_of_Energy}`

---

## Follow the Flock
- Location OSINT (New Haven, CT)

**Flag:** `CIT{State_Street_New_Haven_CT}`

---

# 🧠 Notes

- Each challenge demonstrates a different CTF skill:
  - Web exploitation
  - Crypto analysis
  - Forensics investigation
  - Reverse engineering
  - OSINT

- Tools commonly used:
  - Burp Suite
  - Wireshark
  - StegSolve
  - hashcat
  - binwalk
  - Cheat Engine
  - Ghidra

---