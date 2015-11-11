import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Welcome(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(5)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_to_create_scrapbook(self):
		# Opens Firefox and inputs the URL localhost:8000
		self.browser.get('localhost:8000/')

		# Notices a the browser title labeled Welcome
		self.assertIn("A Life's Journey - Welcome", self.browser.title)

		# She reads the header text Welcome
		header_h1_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn("A Life's Journey", header_h1_text)

		# reading further after the header the text
		p_text=self.browser.find_element_by_tag_name('p').text
		self.assertIn("Keeping memories that's better than ever.", p_text)

		# and notices the text Create Scrapbook

		create_link = self.browser.find_element_by_tag_name('a')
		self.assertIn('Create Scrapbook',create_link.text)
		# better to use find_elements later when other functionalities are added later on

		import time
		time.sleep(3)

		# when she left-clicks the Create Scrapbook text
		create_link.click()
		# or when she presses TAB and ENTER
		# create_link.send_keys(Keys.ENTER)


		# another page opens, this time it is the Create Scrapbook page

		# She notices the browser title labeled Create Scrapbook
		self.assertIn('Create Scrapbook', self.browser.title)

		# She reads the header text Create Scrapbook
		create_header_h1 = self.browser.find_element_by_tag_name('h1')
		self.assertIn('Create Scrapbook', create_header_h1.text)

		# She is invited to enter a name of the scrapbook
		name_inputbox = self.browser.find_element_by_name('scrapbook-name')
		self.assertEqual(name_inputbox.get_attribute('type'),'text')

		# She types "Baby Bae" into a text box (Baby Bae is her first-born child
		name_inputbox.send_keys('Baby Bae First Twelve Months')

		# She is asked to enter the start date of the scrapbook by selecting the
		# day, month, and year from the combo boxes

		# She decides on how often she wants to keep track of her life's
		# journey--daily, weekly or monthly.

		# She enters the number of times she wants to upload pictures.
		# For example, she chose "daily", entered 3 as the frequency, and chose
		# "Hours", then she has to upload photos every 3 hours.

		# She needs to provide her email address so that an email can be sent
		# to remind her to upload pictures based on her preferred
		# frequency and mode

		# Finally, after providing all the necessary details, she has decide
		# whether to discontinue or proceed with the creation of the scrapbook

		# When she clicks on the Cancel button, the creation of the scrapbook
		# will be discontinued and she will be shown the main page.

		# But, if she clicks on the Submit button, the scrapbook will be created

		time.sleep(3)

if __name__ == '__main__': #
	unittest.main(warnings='ignore')
