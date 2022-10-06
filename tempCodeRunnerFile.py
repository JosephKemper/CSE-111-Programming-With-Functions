    # except KeyError as Error:
    #     # This code will be executed if the user tries to find 
    #     # a product that is not in the dictionary or product list
    #     print()
    #     print(f"{Error}: unknown product ID in the filename file")
    #     #print(product_code)
        
    # except FileNotFoundError as Error:
    #     # This code will be executed if the user enters
    #     # the name of a file that doesn't exist.
    #     print()
    #     print(f"{Error}: missing file")
    #     print("[Errno 2] No such file or directory: ")
    
    # except PermissionError as perm_err:
    #     # This code will be executed if the user enters the name
    #     # of a file and doesn't have permission to read that file.
    #     print()
    #     print(type(perm_err).__name__, perm_err, sep=": ")
    #     print("You don't have permission to read filename.")
    #     print("Run the program again and enter the name" \
    #             " of a file that you are allowed to read.")