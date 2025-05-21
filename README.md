# Brute Force Password (MD5 / SHA1)

This simple Python script helps you brute-force MD5 or SHA1 hashes using a custom wordlist. It’s a handy tool for ethical hacking, CTFs, or just playing around with hashes for educational purposes.

---

## What It Does

This script takes in:

* A **hash type** (either `md5` or `sha1`)
* A **path to a wordlist file**
* The **hash value** you want to crack

It reads through each line of your wordlist, hashes the word, and checks if it matches the hash you provided. If it finds a match, it prints the original password and exits.

---

## How to Run It

1. Save the script in a file, e.g., `bruteforce.py`
2. Make sure you have a wordlist (like `rockyou.txt`)
3. Open your terminal and run:

```bash
python bruteforce.py
```

You’ll be prompted like this:

```
Which type of hash you want to bruteforce: md5
Enter path to the file to bruteforce with: /path/to/wordlist.txt
Enter Hash Value to Bruteforce: 5f4dcc3b5aa765d61d8327deb882cf99
```

If it finds a match, it’ll print:

```
Found MD5 Password: password
```

Otherwise:

```
Password not in file
```

## Warning

This script is for **educational** and **ethical** use only. Don’t use it on any system or hash that you don’t own or have explicit permission to test. Seriously.
