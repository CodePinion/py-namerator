'''
UserGen Class 
'''

class UserGen():

    def __init__(self,email,max_num):
        
        self. email = email
        self.max_num = max_num


    def StripMail(self):

        '''
        This method Strips an email
        Example:
        1. Email = dev@gmail.com 
            returns: dev
        2. Email = testmail@yahoo.com
            returns: testmail    
        '''

        mail_extract = self.email.split('@')[0]

        return mail_extract

    def GenNumWithMax(self):

        '''
        This method generates a random number considering the maximum number passed to it
        '''

        