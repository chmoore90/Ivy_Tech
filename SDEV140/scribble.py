state_flag = False

while not state_flag:
    state = input("Enter your state in abbreviated form: ")
    if len(state) == 2 and state.isalpha():
        state_flag = True
    else:
        print("Error: Abbreviated form can only have two letters.")

print("Your state is " + state)


while True:
    try:
        state = input("Enter your state in abbreviated form: ")

        if len(state) == 2 and state.isalpha():
            print("Your state is " + state)
            break

        raise ValueError()
    except ValueError:
        print("Error: Abbreviated form can only have two letters.")



# while True:
#     state, err = str(input(""))
#     if err is not None:
#         x = 1
#         print("whoops")
#         break

#     print(x)

#     new_state, err = do_something_with(state)
#     if err is not None:
#         print("uh oh")
#         break

#     try:
#         state = str(input("Enter your state in abbreviated form: "))
#     except:
#         print("")

#     try:
#         if len(state) == 2:
#             print("state is " + state)
#             break
#         raise Exception("uh uh jabroni")
#     except:
#         print("Error: Abbreviated form can only have two letters.")
