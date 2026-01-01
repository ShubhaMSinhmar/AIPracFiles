def order_stall():
    # print("What would you like to have sir")
    order = yield
    while True:
        print(f"Getting {order} ready!")
        order = yield


order = order_stall()
next(order)

# order.send("Pasta")
# order.send("Biryani")


# STUDYING YEILD FROM AND CLOSE 

def english():
    yield "Pasta"
    yield "Pizza"

def hindi():
    yield "Tea"
    yield "Mishri"

def both():
    yield from english()
    yield from hindi()

for item in both():
    print(item)