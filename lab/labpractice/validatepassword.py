while True:
    pwd = input("enter password")
    has_upper = has_lower = has_digit = has_special = False
    for ch in pwd:
        if ch.islower():
            has_lower = True
        if ch.isupper():
            has_upper = True
        if ch.isdigit():
            has_digit = True
        if not ch.isalnum():
            has_special = True
    if len(pwd) > 8 and has_special and has_digit and has_lower and has_upper:
        print("valiid")
        break
    else:
        print("invalid")
