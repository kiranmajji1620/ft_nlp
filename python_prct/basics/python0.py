def f():
    try:
        # i = int("hai")
        return    
    except OSError:
        pass
    finally:
        print("Hello world")

f()