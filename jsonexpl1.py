import json

# nums = [1,2,23,4,1423,25,345,34,5,341]

# filename = 'nums.json'
# with open(filename, "w") as f:
#     json.dump(nums, f)




# fname = 'nums.json'
# with open(fname) as fl:
#     nums_new = json.load(fl)

# print(nums_new)





# username = input("Name: ")

# filename = 'user.json'

# with open(filename, 'w', encoding="utf-8") as fl:
#     json.dump(username, fl, ensure_ascii=False)
#     print("yyyy " + username + "!")

# with open (filename) as f:
#     user = json.load(f)
#     print("wlcome " + user + "!")






# filename = 'user.json'
# try:
#     with open (filename) as f:
#         user = json.load(f)
# except:
#     username = input("Name: ")
#     with open(filename, 'w', encoding="utf-8") as fl:
#         json.dump(username, fl, ensure_ascii=False)
#         print("yyyy " + username + "!")
# else:
#     print("wlcome " + user + "!")








# def get_user():
#     filename = 'user.json'
#     try:
#         with open(filename) as f:
#             user = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return user


# def greet_user():
#     username = get_user()
#     if username:
#         print("Welcome" + username + "!")
#     else:
#         username = input("Name: ")
#         filename = 'user.json'
#         with open(filename, 'w', encoding="utf-8") as fl:
#             json.dump(username, fl, ensure_ascii=False)
#             print("yyyy " + username + "!")

# greet_user() 














#################new не работает
# people_string = {
#     "people": [
#         {
#             "name" : "Bishkek Baatyr",
#             "phone" : "+9960000000000",
#             "emails" : ["batya@bat.com", "batr@bat.com",],
#             "lisense" : "False",
#         },
#         {
#             "name" : "B B",
#             "phone" : "+9960232323000",
#             "emails" : "null",
#             "lisense" : "True",
#         }
#     ]
# }


# data = json.loads(people_string)

# print(data)