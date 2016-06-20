from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Babs heard about a cool new online to-do app. 
        #She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices that the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # She types "Start boxing again" into a text box 
        inputbox.send_keys('Start boxing again') 

        # When she hits enter, the page updates, and now it lists 
        # "1: Start boxing again" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Start boxing again' for row in rows),
            "New to-do item did not appear in table"
        )

        # There's still a text box inviting her to add another item
        # She enters "Buy nicer goggles for swimming"
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her list

        # Babs wonders whether the site will remember her list,
        # but then sees that the site has generated a unique URL 
        # for her, since there's some explanatory text to that effect.  
        # She visits that URL, and, VIOLA!, her to-do list is there 
        # She dances and punches the air, yelling Woooooh!  
        
        browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')

