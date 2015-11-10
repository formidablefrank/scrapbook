from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import selenium

class Welcome(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(15)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_to_create_scrapbook(self):
		#She opens Firefox and inputs the URL localhost:8000
		self.browser.get('localhost:8000')
		
		#She notices a the browser title labeled Welcome
		self.assertIn('Welcome', self.browser.title)
		
		#She reads the header text Welcome
		header_h1_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Welcome', header_h1_text)
		
		#reading further after the header the text...
		# Lorem ipsum dolor sit amet, consectetur adipisicing elit. Esse laborum molestiae nisi officia, qui tempore. Architecto eligendi repellat similique tempora veritatis? Ab error est labore minima? Culpa earum ut veniam?
		p_text=self.browser.find_element_by_tag_name('p').text
		self.assertIn('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Esse laborum molestiae nisi officia, qui tempore. Architecto eligendi repellat similique tempora veritatis? Ab error est labore minima? Culpa earum ut veniam?', p_text)
		
		#and notices the text Create Scrapbook
				
		create_link = self.browser.find_element_by_tag_name('a')
		self.assertIn('Create Scrapbook',create_link.text)
		#better to use find_elements later when other functionalities are added later on
		
		import time
		time.sleep(3)

		#when she left-clicks the Create Scrapbook text
		create_link.click()
		# or when she presses TAB and ENTER 
		#create_link.send_keys(Keys.ENTER)
		
		
		#another page opens, this time it is the Create Scrapbook page
		
		#She notices the browser title labeled Create Scrapbook
		self.assertIn('Create Scrapbook', self.browser.title)
		
		#She reads the header text Create Scrapbook
		create_header_h1 = self.browser.find_element_by_tag_name('h1')
		self.assertIn('Create Scrapbook', create_header_h1.text)
		
		# She is invited to enter a name of the scrapbook
		name_inputbox = self.browser.find_element_by_name('scrapbook-name')
		self.assertEqual(name_inputbox.get_attribute('type'),'text')

		# She types "Baby Bae" into a text box (Baby Bae is her first-born child
		name_inputbox.send_keys('Baby Bae First Twelve Months')
		
		# She is invited to enter a duration of the scrapbook
		#...
		
		
		
		
		time.sleep(3)

		


if __name__ == '__main__': #
	unittest.main(warnings='ignore')
