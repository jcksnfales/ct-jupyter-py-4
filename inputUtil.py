def req_string(prompt, error="Invalid input. Please input a valid string."):
    '''
    Takes a given 'prompt' and optional 'error' message; asks the user to input a valid String value.
    If a valid String value is not given, presents the user with the defined 'error' message and prompts
    them again for a valid input. Repeats until a valid input is provided, then returns the valid input. 
    '''
    usr_in = None
    while True:
        try:
            # get user input; if the input cannot be cast to an string, it is invalid and will throw an error
            usr_in = str(input(prompt))
            # if the input can be cast to a string, it is valid; break out of this loop
            break
        except:
            # if an error is caught, print 'error' message and continue loop
            print(error)
    return usr_in

def req_int(prompt, valid_range=None, error="Invalid input. Please input a valid integer value."):
    '''
    Takes a given 'prompt', optional 'valid_range' (must be a list/tuple with length of 2 if given),
    optional 'error' message; asks the user to input a valid integer value.
    If a valid integer value is not given, presents the user with the defined 'error' message and prompts
    them again for a valid input. Repeats until a valid input is provided, then returns the valid input. 
    '''
    usr_in = None
    while True:
        try:
            # get user input; if the input cannot be cast to an int, it is invalid and will throw an error
            usr_in = int(input(prompt))
            # if 'range' is not defined and 'usr_in' was successfully cast to int, break out of this loop 
            if not valid_range:
                break
            # if 'range' is defined, make sure 'usr_in' is within it before breaking out of loop
            elif valid_range and usr_in >= valid_range[0] and usr_in <= valid_range[1]:
                break
            # if 'range' is defined but 'usr_in' lies outside it, print an error and return to 
            elif valid_range:
                print(f"Invalid input. Number must be within the range {valid_range}.")
        except:
            # if an error is caught, print 'error' message and continue loop
            print(error)
    return usr_in