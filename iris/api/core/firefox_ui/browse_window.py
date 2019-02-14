# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from iris.api.core.pattern import Pattern


class BrowseWindow(object):
    SEARCH_FIELD = Pattern('browse_window_search_field.png')
    BACKUP_FILE = Pattern('backup_file.png')
    ALL_FILES = Pattern('all_files_option.png')
    JSON = Pattern('json_option.png')
    FILE_TYPE_LIST = Pattern('file_type_list.png')
    FILE_TYPE_OPTIONS = Pattern('file_type_options_button.png')
    OPEN_BUTTON = Pattern('open_file.png')
    OK_BUTTON = Pattern('ok_button.png')