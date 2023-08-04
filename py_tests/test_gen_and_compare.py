import sys

sys.path.insert(1, './/Code')

import generate

email = 'example@gmail.com'
max_number = 100
max_names_gen = 10
custom_list = ['example10','example23']

def test_gen_and_compare():

    user_gen_class = generate.UserGen(email,max_number)

    print(user_gen_class.GenAndCompare(max_names_gen,custom_list))


if __name__ == "__main__":
    test_gen_and_compare()    
    print("Successfully Generated")