import time
import sys
def delay_print(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

def main():
    delay_print("Welcome to my CTF challenge. You will be asked to do OSINT on a popular figure. As you obtain this information, you can enter it into the terminal, and will be given an encoded section of the flag.")
    
if __name__ == "__main__":
    main()
