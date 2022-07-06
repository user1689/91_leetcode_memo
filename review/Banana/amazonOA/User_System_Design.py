from typing import List

class solution:
    def userSystem(self, operations:List[int]) -> None:
        # use map to store user information
        map = dict()
        for opt in operations:
            tmp = opt.split(' ')
            action = tmp[0]
            username = tmp[1]
            password = tmp[2] if len(tmp) > 2 else ""
            # register
            if (action == "register"):
                if (username in map):
                    print("register failed")
                else:
                    if (password == ""):
                        print("register failed")
                    else:
                        map[username] = [password, 0]
                        print("register success")
            # login
            elif (action == "login"):
                if (username not in map):
                    print("login failed")
                else:
                    if (password != ""):
                        if (map[username][1] == 1):
                            print("login failed")
                        else:
                            if (password != map[username][0]):
                                print("login failed")
                            else:
                                map[username][1] = 1
                                print("login success")
                    else:
                        print("login failed")
            # logout
            elif (action == "logout"):
                if (username not in map):
                    print("logout failed")
                else:
                    if (map[username][1] == 0):
                        print("logout failed")
                    else:
                        map[username][1] = 0
                        print("logout success")
                    

obj = solution()
operations = [
    "register david david123",
    "register adam 1Adam1",
    "login david david123",
    "logout david",
    "login david david123",
    "login adam 1adam1",
    "logout david",
    "logout adam",
    "logout apple",
    "register banana",
    "logout zzz zzz",
    "register aa",
    "login zvvv",
    "register aa z",
    "login aa"
]
operations2 = [
    "register adam 1Adam1",
    "login adam 1adam1",
    "logout adam"
]
res = obj.userSystem(operations2)
print(res)