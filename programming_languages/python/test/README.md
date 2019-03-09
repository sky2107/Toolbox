# UNITTEST in python

> import for a parent folder 

    import sys
    sys.path.append('..\\')

    f  rom User import User

> Unittest example
import unittest
from User import User


    # all methods beginning with test will be executed
    class UserTest(unittest.TestCase):
        '''
        User Testing class
        '''
        # global parameter
        email = 'felix.navas@susiandjames.com'
        pwd = ''
        user = None

        def setUp(self):
            '''setUp is called before every test'''
            UserTest.user = User(UserTest.email, UserTest.pwd)

        def tearDown(self):
            '''tearDown is called at the end of every test'''        
            pass

        def testLogin(self):
            token = UserTest.user.token 
            self.assertNotEqual(token, None)
            
    if __name__ == '__main__':
        unittest.main()