# DO NOT MODIFY THIS FILE

# primes in descending order
prime_sizes = [403,203,101,47,23,11,5,2]

def set_primes(list_of_primes):
    global prime_sizes
    prime_sizes = list_of_primes
    
def get_next_size():
    return prime_sizes.pop()
        
# Whenever you need to rehash, call get_next_size() to get the new table size