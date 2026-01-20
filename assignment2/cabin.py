def cabin_description():
    
    try:
        cabin_class = input("Enter the cabin class: ").upper()
    except EOFError:
        print("No input provided.")
        return
        
    if cabin_class == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("Above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("Windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")


cabin_description()
