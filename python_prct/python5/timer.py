import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        after = time.time()
        print(f"function took : {after - before}")
    return wrapper

@timer
def run():
    time.sleep(2)

@timer
def run_list():
    l = [i for i in range(1000)]
    
run()
run_list()