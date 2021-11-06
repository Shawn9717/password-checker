import unittest #import the unittest testing module
from user import User #import user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating tests
    '''

    def setUp(self):
        """
        Set up method to run before each test case.
        """
        self.user_list = User("shawn","njoga","0722348613","shawnnjoga@gmail.com","password")


    def test_init(self):
        """
        Test to see if the object is properly initialized
        """

        self.assertEqual(self.user_list.first_name,"shawn")
        self.assertEqual(self.user_list.last_name,"njoga")
        self.assertEqual(self.user_list.phone_number,"0722348613")
        self.assertEqual(self.user_list.email,"shawnnjoga@gmail.com")
        self.assertEqual(self.user_list.password,"password")
if __name__ == '__main__':
    unittest.main()   