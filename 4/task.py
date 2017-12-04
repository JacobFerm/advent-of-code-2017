import operator

PRIMES = { 'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 
  'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o':  47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 
  't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101 }

def calc_valid_passphrases(input):
    lines = input.splitlines()
    passphrases = map(lambda x: x.split(), lines)
    valid = filter(lambda x: len(x) == len(set(x)), passphrases)
    return len(valid)

def calc_prime_product(word):
    primes = map(lambda x: PRIMES[x], word)
    return reduce(operator.mul, primes, 1)

def map_to_prime_products(list_of_words):
    return map(calc_prime_product, list_of_words)

def calc_valid_passphrases2(input):
    lines = input.splitlines()
    passphrases = map(lambda x: x.split(), lines)
    prime_sums = map(map_to_prime_products, passphrases)
    valid = filter(lambda x: len(x) == len(set(x)), prime_sums)
    return len(valid)

with open ('4/input.txt') as inputFile:
    input = inputFile.read()

print calc_valid_passphrases(input)
print calc_valid_passphrases2(input)