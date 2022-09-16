from module_ex1 import module_fun


def access():
    module_fun()
    print("Hello this is in another file called module_access1.py which is using module_ex1.py "
          "to import it's function.")


access()
