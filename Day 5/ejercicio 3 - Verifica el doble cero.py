def dobles(*args):

    escaneo = 0
    for n in args:

        if escaneo + 1 == len(args):
            return False
        elif args[escaneo] == 0 and args[escaneo + 1] == 0:
            return True
        else:
            escaneo += 1
    return False


print(dobles(6,4,1,254,5,3,7,6,87,85,9,7,4,0))