# yield helps to save memory and we pause from where we at 

def carNames():
    yield "BMW"
    yield "Audi"
    yield "McLaren"

getStuff  = carNames()

# print(next(getStuff))
# print(next(getStuff))
# print(next(getStuff))

# PROJECT -> INFINITE generator show name of the person who want refils and the number of refils


def getRefilBro(name):
    refil = 1
    while True:
        yield f"{name} refil cup {refil}"
        refil += 1
    
SahilOrder = getRefilBro("Sahil")
SameekshaOrder = getRefilBro("Sameeksha")

# for _ in range(5):
#     print(next(SahilOrder))
    
# for _ in range(10):
#     print(next(SameekshaOrder))