# using string function we are going to create code for email checker

email = input("Enter your Email Address: ") # conditions of gmail = g@g.in/.com etc
k,j,d=0,0,0
if len(email)>=6: #1 condition
    if email[0].isalpha(): #2 condition
        if ("@" in email) and (email.count("@")==1): #3 condition
            if (email[-4]==".") ^ (email[-3]=="."): #4 condition
                for i in email:
                    if i==i.isspace(): #5 condition
                        k=1
                    elif i.isalpha():
                        if i==i.upper(): #5 condition
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else: #5 condition
                        d=1
                if k==1 or j==1 or d==1:
                    print(" Error 5 = You Have Wrong Email ")
                else:
                    print("You Have the Right Email Address Format")
            else:
                print(" Error 4 = You Have Wrong Email ")
        else:
            print(" Error 3 = You Have Wrong Email ")

    else:
        print(" Error 2 = You Have Wrong Email ")
else:
    print(" Error 1 = You Have Wrong Email ")

# add more functionality through every kind of email
