from django.test import TestCase
from .models import Profile,Projects
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestCases(TestCase):
    """
    This will test the profiles
    """

    def setUp(self):
        """
        This will add a new profile before each test
        """
        self.new_user = User(username="Hey")
        self.new_user.save()

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_is_instance(self):
        """
        This will test whether the new profile is an instance of the Profile class
        """
        self.assertTrue(isinstance(self.new_user.profile, Profile))

    def test_init(self):
        """
        This will test whether the new profile is created coreectly
        """
        self.assertTrue(self.new_user.profile.bio == "Hi!")

    def test_save_users(self):
        """
        This will test whether the search function works
        """
        users = Profile.save_user("hey")
        self.assertTrue(len(users) == 1)
class projectTestClass(TestCase):

    def test_is_instance(self):
        self.assertTrue(isinstance(self.project,Projects))

    def test_save_method(self):
        """
        function that tests whether an image is saved to database
        """
        projects = Projects.objects.all()
        self.save_project()
    
        
        