import time
import sys
import re

def delay_print(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print("\n")

def ask(question, answer):
    delay_print(question)
    user_answer = input("> ")
    if answer.match(user_answer):
        return True
    else:
        return False

def main():
    delay_print("Welcome to my CTF challenge. You will be asked to do OSINT on a popular figure. As you obtain this information, you can enter it into the terminal, and will be given an encoded section of the flag.")
    question1 = "What is Bill Gates Address?"
    answer1 = re.compile(r"1835\s?73rd\s?Ave\s?NE,?(\s?Medina,?\s?Washington,?\s?USA)?", re.IGNORECASE)
    loop1 = ask(question1, answer1)
    while loop1 is False:
        delay_print("Try Again!")
        loop1 = ask(question1, answer1)
    delay_print("Congradulations! Here is the first encoded section: jbn101{MOLE")
    time.sleep(0.2)

    question2 = "How many kids does he have?"
    answer2 = re.compile(r"3|(three)", re.IGNORECASE)
    loop2 = ask(question2, answer2)
    while loop2 is False:
        delay_print("Try Again!")
        loop2 = ask(question2, answer2)
    delay_print("Congradulations! Here is the second encoded section: _KSUMD_")
    time.sleep(0.2)

    question3 = "What is Bill Gates favorite Dessert?"
    answer3 = re.compile(r"(toll)?\s?(house)?\s?cookies?", re.IGNORECASE)
    loop3 = ask(question3, answer3)
    while loop3 is False:
        delay_print("Try Again!")
        loop3 = ask(question3, answer3)
    delay_print("Congradulations! Here is the third encoded section: WULEPDMTWWRLEPDM}")
    time.sleep(0.2)

    question4 = "What's his nickname?"
    answer4 = re.compile(r"trey", re.IGNORECASE)
    loop4 = ask(question4, answer4)
    while loop4 is False:
        delay_print("Try Again!")
        loop4 = ask(question4, answer4)
    delay_print("Congradulations! Here is the cipher key: BILLGATES (hint: the cipher method was created by two different people independently who did not realize someone else had also come up with it. )")
    time.sleep(0.2)
    
    question5 = "Enter the flag here"
    answer5 = re.compile(r"itc101{BILL_GATES_LOLLLLLLLLLLLLLL}")
    loop5 = ask(question5, answer5)
    while loop5 is False:
        delay_print("Try Again!")
        loop5 = ask(question5, answer5)
    delay_print("Correct!!! Here is your reward:")
    delay_print("https://youtu.be/c6DbXIoSxaM")
    time.sleep(10)
 

if __name__ == "__main__":
    main()
