1. Make sure you have python3 installed

2. First you have to install all the requirements so,
    pip install -r requirements.txt

3. There are only four Route (one is admin)

4. Authentication:-
    Basic Auth:-
    username = "Phone_Number",
    password = "Password"
    (*Provided at time of registration)

5. For register:-
    EndPoint:- api/register/
    Method:- POST
    json_data = {
        "first_name" = String
        "last_name" = String
        "phone" = String
        "email" = String(optional)
        "password" = String(len >= 8)
    }
6. For Spam:-
    EndPoint:- api/spam/
    Method:- GET, POST

    GET:-
    json_data = {
        "phone": String
    }
    Response = {
        "phone": String
        "Count": Integer(Number of user declare it as spam)
    }

    POST:-
    (Declare it as spam)
    json_data{
        "phone": String
    }

7. Search:-
    EndPoint:- api/search/
    Method:- GET
    json_data{
        "query": String
    }

    Response:-
    json_data ["start_with" : {
        "first_name": String,
        "last_name": String,
        "phone": String,
        "Spam_status": String (No, Likely, Most Likely)
        "email": Email (if present in the contact)
    },
    "contain": {
        "first_name": String,
        "last_name": String,
        "phone": String,
        "Spam_status": String (No, Likely, Most Likely)
        "email": Email (if present in the contact)
    }]


8. I also include a script for registration dummy data and to insert data in global contact list(user contact)
    in "generate_data.py" for testing purposes.


Note:-
1. If a user declare any number as spam then he can't do it again
2. Criteria for declare a number spam :-
         1. count = count of user declare a number spam
                if count < 10 -> No Spam
                else if 10 < count < 20 -> Likely
                else count > 20 -> More Likely


