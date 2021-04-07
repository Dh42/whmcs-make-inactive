import requests
import json


# Your API creds
identifier = "xxxx"
secret = "xxxx"
# Your website API url
url = "xxxx"


# keep track of iterations
i = 1
# just a debug to see how many are active while its running
j = 1
#Set to the number of toatl clients in your shop
numclients = xxx
while i < numclients:
    # Forming the client request
    params = {
        'identifier': identifier,
        'secret': secret,
        'action': "GetClientsDetails",
        'clientid': i,
        'stats': 'true',
        'responsetype' : 'json',
        }

# Sending the request
    r = requests.post(url, params=params)
    answer = r.text
    answer_formatted = json.loads(answer)
    #print(answer_formatted)
    if answer_formatted['result'] == "success":
        r = requests.post(url, params=params)
        answer = r.text # this returns a big string, you need to convert it into json if you want to use the answer in any way
        answer_formatted = json.loads(answer)
        print(answer_formatted["email"])
        print(answer_formatted["status"])
        print(answer_formatted["stats"]["grossRevenue"])
        print(answer_formatted["stats"]["isAffiliate"])
        # If revenue is 0 AND user is not an affiliate we set them to inactive
        if answer_formatted["stats"]["grossRevenue"] == "$0.00 USD" and answer_formatted["stats"]["isAffiliate"] == False:
            print(j)
            # The number of active users so far
            j += 1
            # Build the data to make the client inactive
            params = {
                'identifier': identifier,
                'secret': secret,
                'action': "UpdateClient",
                'clientid': i,
                'status': "Inactive",
            }
            # Sending the request to set the user inactive
            r_i = requests.post(url, params=params)
    i += 1
