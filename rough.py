from proj import chatbook



# lst = [1,2]
# a = len(lst)

# print(user.__name)

# print(user._chatbook__name)
# getter and setter -------------------------

# print(user.get_name())

# user.set_name("prash")

# print(user.get_name())
# ------------------------------------------
# static values

# user = chatbook()
# print(user.id)
# user2 = chatbook()
# print(user2.id)
# user3 = chatbook()
# print(user3.id)

# ----------------------------------------------
# static method

user = chatbook()
print(user.id)

chatbook.set_id(20001)

user2 = chatbook()
print(user2.id)

