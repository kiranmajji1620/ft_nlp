from collections import defaultdict

class myDict(dict):
    def __init__(self):
        pass
    
    # def __getitem__(self, key):
    #     print("Get item called")
    

    def __missing__(self, key):
        print("Missing key")

def main():
    # d = {}
    # # print(d[1])
    # a = d.setdefault(1, "Sai")
    # print(a)
    # print(d[1])

    # d = defaultdict(lambda: [1, 2])
    # d[1] = "kiran"
    # a = d[1]
    # print(a)
    d = myDict()
    print(d[0])

if __name__ == "__main__":
    main()