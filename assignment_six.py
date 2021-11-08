def get_max():
    """
    gets the highest number for the lists
    :return:
    """
    x = int(input("What is the highest number you would like to find primes bellow"))
    return x

def gen_list(x):
    """
    generates list of numbers from 2 to the max number
    :param x:
    :return:
    """
    t = 1
    list_one = []
    while t < x:
        t = t + 1
        list_one.append(t)
    return list_one

def primes(list_one):
    """
    Finds the numbers that aren't prime and deletes them
    adds the primes from list one to list two
    :param list_one:
    :return:
    """
    list_two = []
    while len(list_one) > 0:
        testing = list_one[0]
        list_two.append(list_one[0])
        for x in range(len(list_one)):
            if list_one[x] % testing == 0:
                list_one.pop(x)
    return list_two

def main():
    """
    calls all the functions
    :return:
    """
    x = get_max()
    list_one = gen_list(x)
    print("Original list:", list_one)
    print("Primes list:", primes(list_one))



if __name__ == '__main__':
    main()