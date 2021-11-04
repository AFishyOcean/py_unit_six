def get_max():
    x = int(input("What is the highest number you would like to find primes bellow"))
    return x

def gen_list(x):
    t = 1
    list_one = []
    while t < x:
        t = t + 1
        list_one.append(t)
    return list_one

def primes(list_one, x):
    list_two = []
    size = len(list_one)
    while size > 0:
        if list_one[:] % list_one[0] > 0:
            list_two.append(list_one[])
            list_one.pop[]
            size = len(list_one)

def main():
    x = get_max()
    list_one = gen_list(x)
    print("Original list:", list_one)
    print("Primes list:", primes(list_one, x))



if __name__ == '__main__':
    main()