# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self):
        BaseTest.__init__(self)
        self.meta = "Open a bookmark in a New Tab from 'Mozilla Firefox' section"
        self.test_case_id = "163231"
        self.test_suite_id = "2525"
        self.locale = ["en-US"]
        self.exclude = [Platform.MAC]

    def run(self):
        firefox_menu_bookmarks_pattern = Pattern('firefox_menu_bookmarks.png')
        mozilla_firefox_predefined_bookmarks_pattern = Pattern('mozilla_firefox_predefined_bookmarks.png')
        mozilla_firefox_bookmarks_folder_pattern = Pattern('mozilla_firefox_bookmarks_folder.png')
        mozilla_about_us_bookmark_pattern = Pattern('mozilla_about_us_bookmark.png')
        mozilla_about_us_page_pattern = Pattern('mozilla_about_us_page.png')
        context_menu_open_in_a_new_tab_pattern = Pattern('context_menu_open_in_a_new_tab.png')

        open_firefox_menu()

        firefox_menu_bookmarks_exists = exists(firefox_menu_bookmarks_pattern, DEFAULT_FIREFOX_TIMEOUT)
        assert_true(self, firefox_menu_bookmarks_exists, 'Firefox menu > Bookmarks exists')

        click(firefox_menu_bookmarks_pattern)

        mozilla_firefox_bookmarks_folder_exists = exists(mozilla_firefox_bookmarks_folder_pattern,
                                                         DEFAULT_FIREFOX_TIMEOUT)
        assert_true(self, mozilla_firefox_bookmarks_folder_exists, 'Firefox menu > Bookmarks > Mozilla Firefox '
                                                                   'bookmarks folder exists')
        click(mozilla_firefox_bookmarks_folder_pattern)

        mozilla_firefox_predefined_bookmarks_exists = exists(mozilla_firefox_predefined_bookmarks_pattern,
                                                             DEFAULT_FIREFOX_TIMEOUT)
        assert_true(self, mozilla_firefox_predefined_bookmarks_exists, 'Predefined Mozilla Firefox related bookmarks '
                                                                       'displayed')

        right_click(mozilla_about_us_bookmark_pattern)

        context_menu_open_in_a_new_tab_option_displayed = exists(context_menu_open_in_a_new_tab_pattern,
                                                                 DEFAULT_FIREFOX_TIMEOUT)
        assert_true(self, context_menu_open_in_a_new_tab_option_displayed, 'Context menu Open in a New Tab option '
                                                                           'is displayed')

        click(context_menu_open_in_a_new_tab_pattern)

        select_tab(2)

        mozilla_about_us_page_displayed = exists(mozilla_about_us_page_pattern, DEFAULT_SITE_LOAD_TIMEOUT)
        assert_true(self, mozilla_about_us_page_displayed, 'The website related to the selected bookmark is opened in'
                                                           ' the a new tab.')
