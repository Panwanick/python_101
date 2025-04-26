identification = {
    "879023": "DGA879028",
    "879024": "DGH879027",
    "879025": "DGS879026",
    "879028": "DGN879022"
}

print("Welcome to the Republic of Deland's Government Service Program")

user_id = input("Please enter your resident identification number: ")
if user_id in identification:
    user_laser = input("Please enter your resident laser number: ")
    if user_laser == identification[user_id]:
        print("Welcome to the Republic of Deland's Government Service Program. Please select your intended government service:")
        print("1: Apply for Renewal of Residency Card")
        print("2: Apply for Citizenship")
        print("3: Revoke your Residency Status")
        
        service_select = input("Please select your service (1/2/3): ")
        
        if service_select == "1":
            confirm1 = input("Confirm: Y/N ").upper()
            if confirm1 == "Y":
                print("You've renewed your residency for 3 years. Thank you.")
            elif confirm1 == "N":
                print("You've cancelled your residency renewal. Thank you.")
        
        elif service_select == "2":
            confirm2 = input("Confirm: Y/N ").upper()
            if confirm2 == "Y":
                print("You've applied for citizenship. Please wait for approval.")
            elif confirm2 == "N":
                print("You've cancelled your citizenship application. Thank you.")
        
        elif service_select == "3":
            confirm3 = input("Confirm: Y/N ").upper()
            if confirm3 == "Y":
                print("You've revoked your residency. Please wait for approval.")
            elif confirm3 == "N":
                print("You've cancelled the revocation of residency. Thank you.")
        
        else:
            print("Invalid service selection.")
    else:
        print("Your laser number is incorrect, please try again.")
else:
    print("Your ID number is incorrect. Please try again.")
