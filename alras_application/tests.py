from django.test import TestCase, LiveServerTestCase
from django.urls import reverse
from alras_application.models import LabRoom, RoomSlot
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .forms import ReserveSlotForm, CreateUserForm
from .models import Student, LabRoom
from django.contrib.auth.models import User

'''
#Unit Tests
class HomepageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):  
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "alras_application/index.html")

    def test_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "Welcome to Automated Lab Room Allocation System")
        self.assertNotContains(response, "Not on the page")

class LabRoomDetailViewTest(TestCase):
    def setUp(self):
        # Create a post for testing
        self.roomslot = RoomSlot.objects.create(slot='slot-1',title='Test slot')
        self.labroom = LabRoom.objects.create(title='Test Post',slot=self.roomslot)

    def test_labroom_detail_view(self):
        # Test that the post detail view returns a 200 status code,
        # uses the correct template, and contains the post title
        response = self.client.get(reverse('labroom-detail', args=[self.labroom.id,"2023-11-25"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alras_application/labroom_detail.html')
        self.assertContains(response, 'Test Post')


'''


# Testing with Selenium WebDriver

class TestSignup(LiveServerTestCase):

    def setUp(self):
        print("Starting")
        #self.driver = webdriver.Chrome('chromedriver/chromedriver.exe')
        self.driver = webdriver.Firefox()
       
    def test_signup_fire(self):
        #self.driver = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        self.driver.find_element("name", "username").send_keys("Student4")
        self.driver.find_element("name", "password").send_keys("Abra1234")
        self.driver.find_element("name", "loginbutton").click()
        self.assertIn("http://127.0.0.1:8000/accounts/profile/", self.driver.current_url)


    def test_valid_form(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        self.driver.find_element("name", "username").send_keys("Student4")
        self.driver.find_element("name", "password").send_keys("Abra1234")
        self.driver.find_element("name", "loginbutton").click()
        self.driver.get("http://127.0.0.1:8000/labroom/2/2023-11-25/reserve_slot/")
        self.assertIn("http://127.0.0.1:8000/labroom/2/2023-11-25/reserve_slot/", self.driver.current_url)
        self.driver.get("http://127.0.0.1:8000/labroom/3/2023-11-28/update_slot/")
        self.assertIn("http://127.0.0.1:8000/labroom/3/2023-11-28/update_slot/", self.driver.current_url)

        
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()