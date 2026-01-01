# so lets make a decorator
from functools import wraps

# def decorator(stuff):
#     @wraps(stuff)
#     def layout():
#         print("Before")
#         stuff()
#         print("After")
#     return layout

# @decorator
# def names():
#     print("Matcha")

# names()
# print(names.__name__)


# ---------------------------------------------------------------

# logging decorator

# def logger(func):
#     @wraps(func)
#     def layout(*arg, **kwargs):
#         print(f"Calling {func.__name__}")
#         result = func(*arg, **kwargs)
#         print(f"Finished {func.__name__}")
#     return layout

# @logger
# def whatYouWannaDriveToday(car, engine="V6"):
#     print(f"WE are driving {car} with engine {engine}")

# whatYouWannaDriveToday("BMW M4")


# ---------------------------------------------------------------

# Auth decorator 

def auth(func):
    @wraps(func)
    def decorator(role):
        if role != "admin":
            print(f"Admin access only, access denied for {role}")
        else:
            return func(role)
    return decorator

@auth
def accessToSystem(role):
    print("Access Granted ADMIN VERIFIED")

accessToSystem("karan")
accessToSystem("admin")