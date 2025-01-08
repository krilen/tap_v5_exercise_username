def main()->None:
    name:str = input("Please enter you name >> ")
    number:int = int(input("Please enter a number >> "))

    print(f"Your name is {name.title()!r} and your number plus one is {str(number+1)!r}.")



if  __name__ == "__main__":
    main()