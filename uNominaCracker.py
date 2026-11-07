#!/usr/bin/env python3

#####################################################
# uNominaCracker v.2.0
# Author: @David_Uton (M3n0sD0n4ld)
# Twitter: https://twitter.com/David_Uton
# Linkedin: https://www.linkedin.com/in/david-uton/
# Github: https://github.com/m3n0sd0n4ld
#####################################################

import sys
import zipfile
import signal
from datetime import datetime
from pathlib import Path
from pwn import log, context

context.log_level = 'error'

LETTER = 'TRWAGMYFPDXBNJZSQVHLCKE'
SHOW_TIME = datetime.now()

BLUE = '\033[94m'
RED = '\033[91m'
GREEN = '\033[92m'
WHITE = '\033[97m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
END = '\033[0m'


def logotype() -> None:
    print(f'''
█──█ ░█▄─░█ █▀▀█ █▀▄▀█ ─▀─ █▀▀▄ █▀▀█ ░█▀▀█ █▀▀█ █▀▀█ █▀▀ █─█ █▀▀ █▀▀█ 
█──█ ░█░█░█ █──█ █─▀─█ ▀█▀ █──█ █▄▄█ ░█─── █▄▄▀ █▄▄█ █── █▀▄ █▀▀ █▄▄▀ 
─▀▀▀ ░█──▀█ ▀▀▀▀ ▀───▀ ▀▀▀ ▀──▀ ▀──▀ ░█▄▄█ ▀─▀▀ ▀──▀ ▀▀▀ ▀─▀ ▀▀▀ ▀─▀▀
		    			by {BOLD}{RED}M3n0sD0n4ld {END}({BOLD}{YELLOW}@David_Uton{END})
    ''')


def extract_zip(file_path: Path, password: str) -> bool:
    with zipfile.ZipFile(file_path) as zf:
        try:
            zf.setpassword(password.encode('utf-8'))
            zf.extractall()
            return True
        except (RuntimeError, zipfile.BadZipFile):
            return False


def handler(sig, frame) -> None:
    log.failure('Exit...')
    sys.exit(0)


def main() -> None:
    signal.signal(signal.SIGINT, handler)

    if len(sys.argv) < 2:
        print('Error: Debes proporcionar un archivo .zip como argumento.')
        sys.exit(1)

    file_zip = Path(sys.argv[1])

    if not file_zip.is_file() or file_zip.suffix.lower() != '.zip':
        print('Error: El archivo no existe o no es un .zip válido.')
        sys.exit(1)

    logotype()
    print(f"{BOLD}[{BLUE}+{END}] Inicio del cracking: {SHOW_TIME.strftime('%d/%m/%Y %H:%M')}{END}")

    status = log.progress('Password testing:')

    for dni_num in range(10000000, 99999999):
        rest = dni_num % 23
        password = f"{dni_num}{LETTER[rest]}"
        status.status(password)

        if extract_zip(file_zip, password):
            final_time = datetime.now()
            print(f"{BOLD}[{GREEN}!{END}] {BOLD}DNI Found!: {password}{END} - Archivos extraídos.")
            print(f"{BOLD}[{BLUE}+{END}] Cracking completado: {final_time.strftime('%d/%m/%Y %H:%M')}{END}")
            print(f"{BOLD}[{YELLOW}*{END}] Presiona {BOLD}Control + C{END} para salir.")
            break
    else:
        print('No se encontró la contraseña en el rango especificado.')


if __name__ == '__main__':
    main()
