import time
import sys
import numpy as np
import cv2 as cv

def delay_print(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print("\n")

def ask(question, answer):
    delay_print(question)
    user_answer = input("> ")
    if user_answer == answer:
        return True
    else:
        return False

def main():
    delay_print("Welcome to my CTF challenge. You will be asked to do OSINT on a popular figure. As you obtain this information, you can enter it into the terminal, and will be given an encoded section of the flag.")
    question1 = "What is Bill Gates Address?"
    answer1 = "1835 73rd Ave NE, Medina, Washington, USA"
    loop1 = ask(question1, answer1)
    while loop1 is False:
        delay_print("Try Again!")
        loop1 = ask(question1, answer1)
    delay_print("Congradulations! Here is the first encoded section: jbn101{MOLE")
    time.sleep(0.2)

    question2 = "How many kids does he have?"
    answer2 = "3"
    loop2 = ask(question2, answer2)
    while loop2 is False:
        delay_print("Try Again!")
        loop2 = ask(question2, answer2)
    delay_print("Congradulations! Here is the second encoded section: _KSUMD_")
    time.sleep(0.2)

    question3 = "What is Bill Gates favorite Dessert?"
    answer3 = "Cookies"
    loop3 = ask(question3, answer3)
    while loop3 is False:
        delay_print("Try Again!")
        loop3 = ask(question3, answer3)
    delay_print("Congradulations! Here is the third encoded section: WULEPDMTWWRLEPDM}")
    time.sleep(0.2)

    question4 = "What's his nickname?"
    answer4 = "Trey"
    loop4 = ask(question4, answer4)
    while loop4 is False:
        delay_print("Try Again!")
        loop4 = ask(question4, answer4)
    delay_print("Congradulations! Here is the cipher key: BILLGATES (hint: the cipher method was created by two different people independently who did not realize someone else had also come up with it. )")
    time.sleep(0.2)
    
    question5 = "Enter the flag here"
    answer5 = "itc101{BILL_GATES_LOLLLLLLLLLLLLLL}"
    loop5 = ask(question5, answer5)
    while loop5 is False:
        delay_print("Try Again!")
        loop5 = ask(question5, answer5)
    delay_print("Correct!!! Here is your reward:")
    time.sleep(0.2)
    delay_print("https://youtu.be/c6DbXIoSxaM")
 

if __name__ == "__main__":
    main()
