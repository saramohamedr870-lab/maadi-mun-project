userinput=int(input("input your choice"))
if userinput==1:
    generate_pass="gdh73%oio*"
    print(generate_pass)
elif userinput==2:
    password=input("Enter your password")
    score=0
    if len(password) <6:
        score+=1
       print("length is less than 6")
    elif len(password) >=6 and len(password)<=10:
        score+=2
        print("length is between 6 and 10")
    else:
        score+=3
        print("length is greater than 10")
    has_digit = False
    has_upper = False

    for i in password:
        if i.isdigit():
            has_digit = True
        if i.isupper():
            has_upper = True
    if has_digit:
        score += 1
        print("contains digit")
    else:
        print("doesn't contain digit")
    if has_upper:
        score += 1
        print("contains capital letter")
    else:
        print("doesn't contain capital letter")
    if score <4:
        print("weak password")
    elif score==4:
        print("medium password")
    elif score>4:
        print("strong password")