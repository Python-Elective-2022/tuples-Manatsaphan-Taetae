'''
create function called skip_tuples that has tuple as input
    return tuple slice
create main fuction
    t = the tuple input value
    print skip_tuples fuction for the value of t
'''
def skip_tuples(tuple):
    return tuple[::2]

def main():
    t = ('I', 'am', 'a', 'test', 'tuple')
    print(skip_tuples(t))

if __name__ == "__main__":
    main()