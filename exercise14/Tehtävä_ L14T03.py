def isthiszero(num):
    try:
        if num == 0:
            print(True)
            return True
        if num < 0 or num >0:
            print(False)
            return False
    except TypeError:
        print("Ei ole numero")


isthiszero(0)
