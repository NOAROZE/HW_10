# The except-try protects the program so that even if there is a problem, it will be able to continue running the program
# even if there is an error in the program the program does not crash it indicates a problem but continues to run
# x: int = 88
# try:
#     if x / 0:
#         print("ok")
# except:
#     print("not ok")
# while True:
#     try:
#         num: int = int(input("enter a number:"))
#         if not 10 < num < 20:
#             raise ValueError(f"{num} not good")
#     except:
#         print("wrong number")
numbers: list[int] = [6, 8, 70, 22]
SENTINEL: int = -999
while True:
    try:
        num: int = int(input("Enter a  number"))
        if num == SENTINEL:
            break
        print(numbers[num])
    except AttributeError:
        print(f"the number is mast to be int")
    except ValueError:
        print(f"the number is mast to be in range")
