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
        self.new_user = User(username="Me")
        self.new_user.save()

    def test_is_instance(self):
        """
        This will test whether the new profile is an instance of the Profile class
        """
        self.assertTrue(isinstance(self.new_user.profile, Profile))

  class projectTestClass(TestCase):

    def test_is_instance(self):
        self.assertTrue(isinstance(self.project,Projects))

    def test_save_method(self):
        """
        function that tests whether an image is saved to database
        """
        projects = Projects.objects.all()
        self.save_project()
    
        
        
