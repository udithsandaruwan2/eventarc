import random

def generate_code():
    # Generate a random number with 5 digits
    random_number = random.randint(100, 999)
    
    # Generate three random numbers to append
    three_random_numbers = ''.join([str(random.randint(0, 9)) for _ in range(3)])
    
    # Combine the prefix, random number, and three random numbers
    code = f"TD{three_random_numbers}"
    
    return code

