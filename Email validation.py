    
# k, j, d = 0, 0, 0

# if len(email) >= 6:
#     if email[0].isalpha():
#         if "@" in email and email.count("@") == 1:
#             if "." in email:
#                 parts = email.split(".")
#                 if len(parts[-1]) >= 2 and len(parts[-2]) >= 2:
#                     for i in email:
#                         if i.isspace():
#                             k = 1
#                         elif i.isalpha() and i.isupper():
#                             j = 1
#                         elif i.isdigit():
#                             continue
#                         elif i in ["_", ".", "@"]:
#                             continue
#                         else:
#                             d = 1

#                     if k == 1 or j == 1 or d == 1:
#                         print("Wrong Email Format")
#                     else:
#                         print("Correct Email Format")
#                 else:
#                     print("Wrong Email Format")
#             else:
#                 print("Wrong Email Format")
#         else:
#             print("Wrong Email Format")
#     else:
#         print("Wrong Email Format")
# else:
#     print("Wrong Email Format")


email = input("Enter your Email: ")
k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:
            if "." in email:
                parts = email.split(".")
                if len(parts[-1]) >= 2 and len(parts[-2]) >= 2:
                    for i in email:
                        if i.isspace():
                            k = 1
                        elif i.isalpha() and i.isupper():
                            j = 1
                        elif i.isdigit():
                            continue
                        elif i in ["_", ".", "@"]:
                            continue
                        else:
                            d = 1

                    if k == 1 or j == 1 or d == 1:
                        print("Wrong Email Format")
                    else:
                        print("Correct Email Format")
                else:
                    print("Wrong Email Format")
            else:
                print("Wrong Email Format")
        else:
            print("Wrong Email Format")
    else:
        print("Wrong Email Format")
else:
    print("Wrong Email Format")
