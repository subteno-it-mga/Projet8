from django.test import TestCase
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch

class bcolors:
    '''
        Class to colorize test in terminal. Green for success and red for fail.
    '''
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

class TestBasicViews(TestCase):

    def test_index(self):
        '''
            Test if the http response for index is fine (code 200).
        '''
        response = self.client.get(reverse('index'))

        if response:
            self.assertEqual(response.status_code, 200)
            print(bcolors.OKGREEN + "TEST_INDEX = OK"+bcolors.ENDC)
        else:
            print(bcolors.WARNING + "TEST_INDEX = FAIL"+bcolors.ENDC)

        try:
            self.client.get(reverse('indexNoReverseMatchError'))
        except NoReverseMatch:
            print(bcolors.OKGREEN + "TEST_INDEX = OK" + bcolors.ENDC)
        

    def test_favorite(self):
        '''
            Test if the http response for favorite page is fine (code 200).
        '''

        if self.client.get(reverse('favorite')):
            self.assertEqual(self.client.get(reverse('favorite')).status_code, 200)
            print(bcolors.OKGREEN + "TEST_FAVORITE = OK" + bcolors.ENDC)

        else:
            print(bcolors.WARNING + "TEST_FAVORITE = FAIL" + bcolors.ENDC)

        try:
            self.client.get(reverse('favoriteNoReverseMatchError'))
        except NoReverseMatch:
            print(bcolors.OKGREEN + "TEST_FAVORITE = OK" + bcolors.ENDC)

# class TestUserAccount(TestCase):

#     def test_post(request):
#         pass

#     def test_login(self):
#         pass

#     def test_logout(self):
#         pass
    
#     def test_signup(self):
#         pass