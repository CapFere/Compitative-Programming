from pyfiglet import figlet_format
from termcolor import colored

from sum import sum
from mult import mult
from div import div

def main():
    color = "green"
    font = "slant" 
    ascii_art = figlet_format("Calculator",font=font)
    colored_ascii = colored(ascii_art,color=color)
    print(colored_ascii)
    while True:
        user_input = input("Enter Command(Operand Operator Operand)(quit: q): ").split()
        if(user_input[0] and user_input[0]=="q"): 
            color = "red"
            font = "slant" 
            ascii_art = figlet_format("E x i t",font=font)
            colored_ascii = colored(ascii_art,color=color)
            print(colored_ascii)
            break
        if(len(user_input)<3):
            print("\nERROR:: Too Few Arguments Expected(3) Got(%s)\n".format(len(user_input)))
            continue
        elif(len(user_input)>3):
            print("\nERROR:: Too Many Arguments Expected(3) Got(%s)\n".format(len(user_input)))
            continue
        elif user_input[2].startswith("0") or user_input[2].startswith("-0"):
            print("\nERROR:: Denominator Can't be Zero\n")
            continue
        elif user_input[0].startswith("0") or user_input[0].startswith("-0"):
            print("\n:: {} / {}  = 0 ::\n".format(user_input[0],user_input[2]))
            continue
            
        first_number = user_input[0]
        operator = user_input[1]
        second_number = user_input[2]

        if operator=="+":
            print("\n:: {} + {}  = {} :\n:".format(first_number,second_number, sum(first_number,second_number)))
        elif operator=="-":
            second = second_number
            if second_number.find("-")!=-1: second_number = second_number[1:]
            else: second_number = "-" + second_number
            print("\n:: {} - {}  = {} ::\n".format(first_number,second, sum(first_number,second_number)))
        elif operator=="*":
            print("\n:: {} x {}  = {} ::\n".format(first_number,second_number, mult(first_number,second_number)))
        elif operator=="/":
            print("\n:: {} / {}  = {} ::\n".format(first_number,second_number, div(first_number,second_number)))
        else:
            print("\nERROR:: Invalid Operator\n")
    
    


if __name__ == '__main__':main()