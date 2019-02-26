# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self):
        BaseTest.__init__(self)
        self.meta = "Cut a bookmark from 'Mozilla Firefox' section"
        self.test_case_id = "163376"
        self.test_suite_id = "2525"
        self.locale = ["en-US"]
        self.exclude = [Platform.MAC, Platform.LINUX]

    def run(self):
        firefox_menu_bookmarks_pattern = Pattern('firefox_menu_bookmarks.png')
        mozilla_firefox_predefined_bookmarks_pattern = Pattern('mozilla_firefox_predefined_bookmarks.png')
        mozilla_firefox_bookmarks_folder_pattern = Pattern('mozilla_firefox_bookmarks_folder.png')
        mozilla_about_us_bookmark_pattern = Pattern('mozilla_about_us_bookmark.png')
        cut_option_pattern = Pattern('cut_option.png')
        paste_option_pattern = Pattern('paste_option.png')
        other_bookmarks_empty_label_pattern = Pattern('other_bookmarks_empty_label.png')

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

        cut_option_exists = exists(cut_option_pattern, DEFAULT_FIREFOX_TIMEOUT)
        assert_true(self, cut_option_exists, 'The Cut option exists')

        click(cut_option_pattern)

        click(Library.OTHER_BOOKMARKS)

        other_bookmarks_empty_label_exists = exists(other_bookmarks_empty_label_pattern, DEFAULT_FIREFOX_TIMEOUT)
        assert_true(self, other_bookmarks_empty_label_exists, 'Other Bookmarks empty label exists')

        right_click(other_bookmarks_empty_label_pattern)

        paste_option_exists = exists(paste_option_pattern, DEFAULT_FIREFOX_TIMEOUT)
        assert_true(self, paste_option_exists, 'Paste option exists')

        click(paste_option_pattern)

        bookmark_pasted = exists(mozilla_about_us_bookmark_pattern, DEFAULT_FIREFOX_TIMEOUT)
        assert_true(self, bookmark_pasted, 'Bookmark is correctly pasted in selected section')

        click(mozilla_firefox_bookmarks_folder_pattern)

        bookmark_deleted = exists(mozilla_about_us_bookmark_pattern)
        assert_false(self, bookmark_deleted, 'Bookmark is correctly deleted from previous section')

        restore_firefox_focus()
