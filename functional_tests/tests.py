import unittest
import selenium
import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


from django.test import LiveServerTestCase

class Welcome(LiveServerTestCase):

	@classmethod
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(51)
		#self.browser.get(self.live_server_url) #dif of this with create_scrapbook?

	@classmethod
	def tearDown(self):
		time.sleep(3)
		#self.browser.quit()

	def test_can_start_to_create_scrapbook(self):
		# Opens Firefox and inputs the URL localhost:8000
		self.browser.get('localhost:8000')

		# Notices a the browser title labeled Welcome
		self.assertIn("A Life's Journey - Welcome", self.browser.title)

		# She reads the header text Welcome
		header_h1_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn("A Life's Journey", header_h1_text)

		# reading further after the header the text
		body_text=self.browser.find_element_by_tag_name('body').text
		self.assertIn("Keeping memories that's better than ever.", body_text)

		# and notices the text Get Started!
		start_link = self.browser.find_element_by_xpath("//*[contains(text(),'Get Started!')]")

		# She clicks the Get Started!
		time.sleep(3)
		start_link.click()

		# She is asked to enter her login credentials
		username_field = self.browser.find_element_by_name('email')
		username_field.send_keys('user@email.com')
		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys('pass')
		login_link = self.browser.find_element_by_link_text('Login')

		# She clicked the Login button
		time.sleep(2)
		login_link.click()

		# This time it is the Create Scrapbook page opens
		# She notices a text "Create A Scrapbook"
		# She decided to create a scrapbook so she click on this link
		create_scrap_link = self.browser.find_element_by_link_text('Create A Scrapbook')
		time.sleep(2)
		create_scrap_link.click()

		# She is invited to enter a name of the scrapbook
		name_inputbox = self.browser.find_element_by_name('name')
		# self.assertEqual(name_inputbox.get_attribute('type'),'text')

		# She types "Baby Bae" into a text box (Baby Bae is her first-born child
		name_inputbox.send_keys('Baby Bae First Twelve Months')

		# She is asked to provide a short description of this new scrapbook
		description_inputbox = self.browser.find_element_by_name('description')

		# She types "Recording memorable events in Baby Bae's First 12 Months"
		description_inputbox.send_keys('Recording memorable events in Baby Bae\'s First 12 Months')


		# She is asked to enter the start date of the scrapbook
		start_date = self.browser.find_element_by_name('start_date')

		# She decides to start on 11/18/2015, Baby Bae's date of birth
		start_date.send_keys('11/18/2015')

		# She decides on how often she wants to keep track of her baby's life
		# journey--daily, weekly or monthly. She chose Monthly
		select_mode = Select(self.browser.find_element_by_name('frequency'))
		select_mode.select_by_visible_text('Monthly')

		# She has to enter the number of times she wants to upload pictures.
		mode_inputbox = self.browser.find_element_by_name('every')
		# For example, she chose "daily", for the mode, she entered 3 and chose
		# "Hours", then she has to upload photos every 3 hours each day.
		mode_inputbox.send_keys('3')

		select_mode = Select(self.browser.find_element_by_name('mode'))
		select_mode.select_by_visible_text('Days')

		# She needs to provide her email address so that an email can be sent
		# to remind her to upload pictures based on her preferred
		# frequency and mode
		email_inputbox = self.browser.find_element_by_name('email')
		email_inputbox.send_keys('user@email.com')

		# Finally, after providing all the necessary details, she has to agree
		# on the terms and conditions and she chose to agree by clicking the
		#check box.
		agree_box = self.browser.find_element_by_name('agree')
		agree_box.click()

		#She clicks on the Submit button and the new scrapbook is created.
		submit_box = self.browser.find_element_by_name('submit')
		submit_box.click()

		time.sleep(3)

		success_message = self.browser.find_element_by_name('success-message').text
		self.assertIn("Success", success_message)

		# THIS SHOULD BE THE UNIT TEST AND IDEALLY IT SHOULD BE PLACED SEPARATELY FROM THE FUNCTIONAL TEST.
		# BUT SINCE ALL TESTS ARE JUST IN ONE FOLDER, I WILL INCLUDE THIS HERE - gushi

		# IF THE SCRAPBOOK WAS SUCCESSFULLY CREATED, THE USER WILL CLICK THE DASHBOARD
		dashboard_link = self.browser.find_element_by_link_text("A Life's Journey")
		dashboard_link.click()

		# AND FIND THE NEW SCRAPBOOK LISTED ON THE SIDE PANEL:
		current_scrapbook = self.browser.find_element_by_link_text('Current: Baby Bae First Twelve Months')
		current_scrapbook.click()
		time.sleep(2)
		current_scrapbook = self.browser.find_element_by_link_text('View Scrapbook')
		current_scrapbook.click()

		print('Create scrapbook functional test completed.')

	def test_can_upload_to_current_scrapbook(self):
		# Opens Firefox and inputs the URL localhost:8000
		self.browser.get('localhost:8000/webapp/dashboard')

		#UPLOAD SEVERAL PHOTOS
		filenames = ['cute-baby-boy-01', 'cute-baby-boy-02', 'cute-baby-boy-03', 'cute-baby-boy-04', 'cute-baby-boy-05', 'cute-baby-boy-06', 'cute-baby-boy-07', 'teddybear']

		for index, filename in enumerate(filenames):
			current_scrapbook = self.browser.find_element_by_link_text('Current: Baby Bae First Twelve Months')
			current_scrapbook.click()
			time.sleep(1)
			# User selects the Upload Photo module
			upload_photo = self.browser.find_element_by_name("uploader")
			time.sleep(1)
			upload_photo.click()
			# User puts the name of the picture
			photo_name = self.browser.find_element_by_name('name')
			photo_name.send_keys("Baby Bae's photo " + str(index))

			# User puts a caption describing the picture
			caption = self.browser.find_element_by_name('caption')
			caption.send_keys("Yo baby Bae so cuuuuute!" + str(index))

			# User uploads a photo. For testing purposes,
			# I placed images to "upload" in webapp/images
			upload_image = self.browser.find_element_by_name("image")
			upload_image.send_keys("~/scrapbook/assets/test_images/" + filename + '.jpg')
			time.sleep(2)

			# IF UPLOAD WAS SUCCESSFUL
			submit_button = self.browser.find_element_by_name('submit')
			submit_button.click()
			time.sleep(1)

		print('Upload photos to scrapbook testing successful.')


	def test_can_view_photos_in_current_scrapbook(self):
		self.browser.get('localhost:8000/webapp/dashboard')
		# AND FIND THE NEW SCRAPBOOK LISTED ON THE SIDE PANEL:
		current_scrapbook = self.browser.find_element_by_link_text('Current: Baby Bae First Twelve Months')
		current_scrapbook.click()
		time.sleep(1)
		view_scrapbook = self.browser.find_element_by_link_text('View Scrapbook')
		view_scrapbook.click()

		view_photo = self.browser.find_element_by_link_text("View")
		view_photo.click()
		time.sleep(2)

		close_photo = self.browser.find_element_by_css_selector(".ui.deny.button")
		print(close_photo)
		self.browser.execute_script('return arguments[0].scrollIntoView();', close_photo)
