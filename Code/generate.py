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
        This method Strips an email

        - It first check if the email format is valid, 
            * if true => it proceeds with the following
                Example:
                1. Email = dev@gmail.com 
                    returns: dev
                2. Email = testmail@yahoo.com
                    returns: testmail   

            * if false 
        '''

        check_valid_mail = bool(re.match(r"[^@]+@[^@]+\.[^@]+", self.email))

        if check_valid_mail == True:

            mail_extract = self.email.split('@')[0]

            return mail_extract

        else:

            raise ValueError('Invalid Email Format : ' + self.email)

    def GenNumWithMax(self):

        '''
        This method generates a random number considering the maximum number passed to it
        '''

        if self.max_num < 1:

            raise ValueError('The maximum number should be greated than 1')
        
        else:

            gen_number =  random.randint(1, self.max_num)

            gen_number = str(gen_number)

            return gen_number
        

    def combine_mail_num(self):

        '''
        This method now combines the stripped email and random number generated
        '''

        return self.StripMail() + self.GenNumWithMax()