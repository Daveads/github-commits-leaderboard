import json

def usersd_list(inputd):
    with open('specific_user_data.json', 'r') as file:
        data = file.read()

    users = json.loads(data)

    if inputd == "username":
        usernames = [user[f"{inputd}"] for user in users]

        return usernames
    
    elif inputd == "email":
        emails = [user[f"{inputd}"] for user in users]
        return emails
