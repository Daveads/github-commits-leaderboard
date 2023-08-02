import json

def usersd_list(inputd):
    with open('specific_user_data.json', 'r') as file:
        data = file.read()

    users = json.loads(data)

    if inputd == "username":
        usernames =  users[0].get('users', [])

        return usernames
    
    elif inputd == "emails":
        emails = users[0].get('emails', [])
        return emails
