def skip_tuples(Tuples):
    return Tuples[::2]

def main():
    t = ('I', 'am', 'a', 'test', 'tuple')
    print(skip_tuples(t))

if __name__ == "__main__":
    main()