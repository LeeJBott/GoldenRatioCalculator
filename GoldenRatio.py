import random
import os
from time import sleep

#[a+b] is to [a] as [a] is to [b]

phi = 1.618

def ratio_a():
    print("[------a(Long)------][---b(Short)---]\n[-------------a+b(Whole)------------]") #Visual Print (for use in CLI)
    ask_a = float(input("Input your measurement (a): "))
    os.system("clear")
    num_flt = float(ask_a)
    if ask_a == num_flt:
        a_num = ask_a * phi
        b_num = a_num - ask_a
        print(f"Golden Ratio Result:")
        print(f"[-----a){round(ask_a, 3)}-----][---b){round(b_num, 3)}---]")
        print(f"[----------a+b){round(a_num, 3)}-----------]")
    else:
        print("Enter your input as a Decimal (eg. 1.0)")

def ratio_b():
    print("[------a(Long)------][---b(Short)---]\n[------------a+b(Whole)-------------]")
    os.system("clear")
    ask_b = float(input("Input your measurement (b): "))
    num_flt = float(ask_b)
    if ask_b == num_flt:
        b_num = ask_b * phi
        a_num = ask_b + b_num
        print(f"Golden Ratio Result:")
        print(f"[-----a){round(b_num, 3)}-----][---b){round(ask_b, 3)}---]")
        print(f"[----------a+b){round(a_num, 3)}----------]")
    else:
        print("Enter your input as a Decimal (eg. 1.0)")

def q_spec():
    while True:
        print("[------a(Long)------][---b(Short)---]\n[------------(Whole(a+b)------------]")
        ask2 = input("Enter Your Reference Measurement (a/b): ")
        if ask2.lower() == "a":
            os.system("clear")
            ratio_a()
            break
        elif ask2.lower() == "b":
            os.system("clear")
            ratio_b()
            break
        else:
            print("Input 'a' or 'b'")
            continue

def intro():
    print("Golden Ratio Calculator")
    sleep(1.5)
    os.system("clear")
    q_spec()

if __name__ == "__main__":
    intro()
