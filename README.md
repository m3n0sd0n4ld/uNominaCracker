<p align="center">
  <img src="logo_uNominaCracker.png" width="500" alt="at0m"/>
</p>

# uNominaCracker

## Credits
###### Author: M3n0sD0n4ld
###### Twitter: [@David_Uton](https://twitter.com/David_Uton)

## Description
**uNominaCracker** is a Python script that performs brute-force attacks on password-protected ZIP files containing payroll documents. It generates candidate passwords by iterating through Spanish DNI numbers and appending the corresponding control letter (using the official `TRWAGMYFPDXBNJZSQVHLCKE` sequence) until the correct combination is found.

## Features
- Fully compatible with **Python 3.12+**.
- Uses **`pathlib`** for safe and modern file handling.
- Employs **f-strings** for faster and cleaner output.
- Specific exception handling for `zipfile` errors (wrong password, corrupt file).
- Colored progress bar and status messages for better UX.
- Graceful interruption with `Ctrl+C`.

## Prerequisites
- **Python 3.12 or higher**
- **pwntools** (for the progress bar and logging)

Install the dependency with:
```console
pip install pwntools
```

# Download and install:
```console
git clone https://github.com/m3n0sd0n4ld/uNominaCracker.git
cd uNominaCracker
python3 uNominaCracker.py FILE.ZIP
```

# Docker version:
## Acknowledgement
Twitter: [@interh4ck](https://twitter.com/interh4ck)
GitHub:(https://github.com/interhack86)

```console
git clone https://github.com/m3n0sd0n4ld/uNominaCracker.git
cd uNominaCracker
docker build -t uNominaCracker .
docker run --rm -it -v 'pathzip':/tmp/ uNominaCracker /tmp/name.zip
```
# Use
The script expects a single argument: the path to the ZIP file you want to crack.

```console
python3 uNominaCracker.py FILE.ZIP
```
The tool will iterate through all possible DNI numbers (from 10000000 to 99999999), compute the correct control letter, and test each password against the ZIP archive. When the correct password is found, the files are extracted to the current directory.

# PoC
```console
root@m3n0sd0n4ld:~# python3 uNominaCracker.py nómina-junio.zip

█──█ ░█▄─░█ █▀▀█ █▀▄▀█ ─▀─ █▀▀▄ █▀▀█ ░█▀▀█ █▀▀█ █▀▀█ █▀▀ █─█ █▀▀ █▀▀█ 
█──█ ░█░█░█ █──█ █─▀─█ ▀█▀ █──█ █▄▄█ ░█─── █▄▄▀ █▄▄█ █── █▀▄ █▀▀ █▄▄▀ 
─▀▀▀ ░█──▀█ ▀▀▀▀ ▀───▀ ▀▀▀ ▀──▀ ▀──▀ ░█▄▄█ ▀─▀▀ ▀──▀ ▀▀▀ ▀─▀ ▀▀▀ ▀─▀▀
                                        by M3n0sD0n4ld (@David_Uton)

[+] Start cracking: 04/10/2020 22:25h
[v] Password testing:: 67214212R
[!] DNI Found!: 66988896Q - The files have been extracted.
[+] Cracking completed: 05/10/2020 12:37h
[*] Press Control + C to exit
[-] Exit ...
```

# Disclaimer
This has been a proof-of-concept project, so the tool is for personal and legitimate use. I AM NOT RESPONSIBLE FOR ITS INAPPROPRIATE USE.
