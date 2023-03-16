def hello():
    print("Hello World!")


def pack(basketball,soccer,football):
    return[basketball,soccer,football]

def eat_lunch(my_lst):
    if len(my_lst) == 0:
        print("My lunchbox is empty!")
        else:
          for i in range(len(my_lst)):
                if i == 0:
                    print(f"First I eat {my_lst[0]}")
                else:
                    print(f"Next I eat {my_lst[i]}")


hello()
print(pack("basketball","soccer","football"))
eat_lunch([])
eat_lunch(["chips"])
eat_lunch(["mango","grapes","chips"])