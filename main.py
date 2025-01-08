def main()->None:
    name:str = input("Please enter you name >> ")
    number:int = int(input("Please enter a number >> "))

    print(f"Your name is {name.title()!r} and your number plus one is {number+1}.")



if  __name__ == "__main__":
    main()