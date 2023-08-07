import sys

sys.path.insert(1, './/Code')

import generate

email = 'example@gmail.com'
max_number = 11
max_names_gen = 10

def test_more_gens():

    user_gen_class = generate.UserGen(email,max_number)

    print(user_gen_class.GenMoreName(max_names_gen))
    

if __name__ == "__main__":
    test_more_gens()
    print("Successfully Generated")