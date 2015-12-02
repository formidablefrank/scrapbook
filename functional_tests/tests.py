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

    def test_suite_all_tests(self):
        self.CreateScrapbook()
        self.UploadToScrapbook()
        self.ViewPhotoInScrapbook()
        self.ArchiveScrapbook()
        self.PublishScrapbook()

    def CreateScrapbook(self): #test_can_start_to_create_scrapbook
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

    def UploadToScrapbook(self): #test_can_upload_to_current_scrapbook
        # Opens Firefox and inputs the URL localhost:8000
        self.browser.get('localhost:8000/webapp/dashboard')

        #UPLOAD SEVERAL PHOTOS
        # filenames = ['cute-baby-boy-01', 'cute-baby-boy-02', 'cute-baby-boy-03', 'cute-baby-boy-04', 'cute-baby-boy-05', 'cute-baby-boy-06', 'cute-baby-boy-07', 'teddybear']
        filenames = ['cute-baby-boy-01', 'cute-baby-boy-02']

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
            caption.send_keys("Yo baby Bae so cuuuuute! " + str(index))

            # User uploads a photo. For testing purposes,
            # I placed images to "upload" in webapp/images
            upload_image = self.browser.find_element_by_name("image")
            upload_image.send_keys("/home/fdd/Desktop/fddd/cs260-AdvancedSoftwareEngineering/project/scrapbook/assets/test_images/" + filename + '.jpg') #just for me (francis)
            
            time.sleep(2)

            # IF UPLOAD WAS SUCCESSFUL
            submit_button = self.browser.find_element_by_name('submit')
            submit_button.click()
            time.sleep(1)

        print('Upload photos to scrapbook testing successful.')


    def ViewPhotoInScrapbook(self): #test_can_view_photos_in_current_scrapbook
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

        
        #close_photo = self.browser.find_element_by_css_selector(".ui.deny.button")
        #self.browser.execute_script("return arguments[0].scrollIntoView();", close_photo)
        #close_photo.click()

        print('View photo in current scrapbook test successful.')

    def ArchiveScrapbook(self): #test_can_archive_current_scrapbook
        self.browser.get('localhost:8000/webapp/dashboard')
        current_scrapbook = self.browser.find_element_by_link_text('Current: Baby Bae First Twelve Months')

        #User clicks archive scrapbook
        current_scrapbook.click()
        time.sleep(1)
        archive_scrapbook = self.browser.find_element_by_link_text('Archive Scrapbook')
        archive_scrapbook.click()
        time.sleep(1)

        #scrapbook is now closed, user should be able to find scrapbook listed as closed
        closed_scrapbooks = self.browser.find_element_by_link_text('View Closed Scrapbooks')
        closed_scrapbooks.click()
        time.sleep(1)

        #user tries to view closed scrapbook
        just_closed_scrapbook = self.browser.find_element_by_link_text('Baby Bae First Twelve Months')
        just_closed_scrapbook.click()
        time.sleep(1)

        #Need a way to test that user cannot upload
        try:
            upload_photo = self.browser.find_elements_by_link_text('Submit')
            self.fail('Can still upload photo! Scrapbook should be uneditable.')
        except:
            print('Submit button not found.')

        #Need a way to test that user cannot delete anymore
        try:
            delete_photo = self.browser.find_elements_by_link_text('Delete')
            self.fail('Can still delete photo! Scrapbook should be uneditable.')
        
        except:
            pass
            print('Closing scrapbook functional test successful.')
    
    def PublishScrapbook(self):
        print("Publishing Scrapbook.")
        self.browser.get('localhost:8000/webapp/dashboard')
        
        closed_scrapbooks = self.browser.find_element_by_link_text('View Closed Scrapbooks')
        closed_scrapbooks.click()
        time.sleep(1)
        
        current_scrapbook = self.browser.find_element_by_link_text('Baby Bae First Twelve Months')
        current_scrapbook.click()
        time.sleep(1)
        
        publish_button = self.browser.find_element_by_link_text('Publish')
        publish_button.click()
        time.sleep(1)
        
        #When the user clicks the Publish button, the save dialog box opens to save the pdf file
		#Since selenium cannot test system-level dialog boxes such as Save As...
		# the test stops here.
		
        #our app does not generate static URL for the pdf file  so the following is not carried out.
        #fp = webdriver.FirefoxProfile()

        #Case:3 - Download to custom folder path. Replace d:\\selenium with your Download Location 
   #     fp.set_preference("browser.download.dir","./assets/scrapbooks/");
    #    fp.set_preference("browser.download.folderList", 2);
     #   fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf");
