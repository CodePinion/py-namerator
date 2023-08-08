'''
UserGen Class 
'''

import random
import re

class UserGen():

    def __init__(self,email,max_num):
        
        self. email = email
        self.max_num = max_num


    def StripMail(self):

        '''
        This method Strips an Email.

        - It first check if the email format is valid, 
            * if true => it proceeds with the following
                Example:
                - Email = dev@gmail.com 
                    returns: dev
                - Email = testmail@yahoo.com
                    returns: testmail   

            * if false => raises a value error
        '''

        check_valid_mail = bool(re.match(r"[^@]+@[^@]+\.[^@]+", self.email))

        if check_valid_mail == True:

            mail_extract = self.email.split('@')[0]

            return mail_extract

        else:

            raise ValueError('Invalid Email Format : ' + self.email)
        

    def GenNumWithMax(self, comparable_number_list=[]):

        '''
        ### This method 
        * Generates a random number considering the maximum number passed to it.
        * Then, converts the generated number to a string => str(generated_number).
        '''

        #Convert the Number list to set for easier searching
        comparable_set = set(comparable_number_list)
        #Set number found to false
        number_found = False

        if isinstance(self.max_num, int):

            if self.max_num < 1:

                raise ValueError('The Maximum Number should be greated than 1')
            
            else:

                while number_found == False:

                    gen_number =  random.randint(1, self.max_num)

                    if gen_number not in comparable_set:

                        gen_number = str(gen_number)

                        number_found = True

                        return gen_number
                    
                    else:
                        
                        number_found = False

        
        else:

            raise ValueError('The Maximum Number should be of type Integer')
        

    def Combine_Mail_Num(self,number_list=[]):

        '''
        This method now combines the stripped email and random number generated
        '''

        return self.StripMail() + self.GenNumWithMax(number_list)
        

    def GenMoreName(self, names_amount, custom_list = [], number_list=[]):

        '''
        ### This method 
        * Generates the amount of names passed (names_amount = )
        * Also gives you the ability to compare the generated names with a (custom list = [ ])
        * Also compares the generated number from the GenNumWithMax(number_list=[]) method with a custom list passed from this method to the GenNumWithMax(number_list=[]) method
        '''

        #Set of generated usernames
        generated_names_set = set()

        #Convert the custom list to find items faster Time Complexity of search in set is O(n)
        custom_list_set = set(custom_list)

        if isinstance(names_amount, int):
        
            if names_amount < 1:

                raise ValueError('The amount of names to be generated cannot be less than 1')
            
            else:

                if names_amount > self.max_num:

                    raise ValueError('The amount of names to be generated cannot be more than the set maximum range of the random numbers generated')
                
                else:

                    loop_count = 0

                    while loop_count < names_amount:

                        name_generated = self.Combine_Mail_Num(number_list)

                        if name_generated not in (generated_names_set | custom_list_set):

                            generated_names_set.add(name_generated)

                            loop_count += 1

                        else:

                            loop_count = loop_count


                #Covert the generated_names_set to a list to be returned
                generated_names = list(generated_names_set)


        else:

            raise ValueError('The amount of names to be generated should be of Integer type')


        return generated_names    