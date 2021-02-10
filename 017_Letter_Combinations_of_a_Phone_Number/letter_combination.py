
def letter(digits):

    combination = []
    phone_number = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    if "1" in digits:
        digits.replace("1" , "") 
    
    if "0" in digits:
        digits.repalce("0", "")

    if digits == "":
        return combination

    all_letters = []
    for x in range(len(digits):

       all_letteres.append(phone_number[digits[x]]) 
    
