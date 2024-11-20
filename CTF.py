import time

def print_slow(string):
    for char in string:
        print(char)
        time.sleep(.25)

def main():
    print_slow("Welcome to my CTF challenge. You will be asked to do OSINT on a popular figure. As you obtain this information, you can enter it into the terminal, and will be given an encoded section of the flag.")

if __name__ == "__main__":
    main()
