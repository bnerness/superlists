from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Babs heard about a cool new online to-do app. She goes to check out its
        # homepage
        self.browser.get('http://localhost:8000')

        # She notices that the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item right away

        # She types "Start boxing again" into a text box 
        # When she hits enter, the page updates, and now it lists 
        
        # "1: Start boxing again" as an item in a to-do list

        # There's still a text box inviting her to add another item
        # She enters "Buy nicer goggles for swimming"

        # The page updates again, and now shows both items on her list

        # Babs wonders whether the site will remember her list,
        # but then sees that the site has generated a unique URL 
        # for her, since there's some explanatory text to that effect.  
        # She visits that URL, and, VIOLA!, her to-do list is there 
        # She dances and punches the air, yelling Woooooh!  
        
        browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')

