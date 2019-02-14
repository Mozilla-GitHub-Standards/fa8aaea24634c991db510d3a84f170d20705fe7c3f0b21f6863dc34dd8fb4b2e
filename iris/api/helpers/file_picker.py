# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.api.helpers.keyboard_shortcuts import *
from iris.api.core.firefox_ui.library import Library
from iris.api.core.firefox_ui.browse_window import BrowseWindow
from iris.api.core.region import *


class FilePicker(object):

    @staticmethod
    def open_browsing_window():
        open_library()

        try:
            wait(Library.IMPORT_AND_BACKUP_BUTTON, 10)
            logger.debug('Import and Backup button is present on the page.')
            click(Library.IMPORT_AND_BACKUP_BUTTON)
        except FindError:
            raise FindError('Import and Backup button is NOT present on the page, aborting.')

        try:
            wait(Library.ImportAndBackup.RESTORE, 10)
            logger.debug('Restore option is present on the page.')
            click(Library.ImportAndBackup.RESTORE, 1)
        except FindError:
            raise FindError('Restore option is NOT present on the page, aborting.')

        try:
            wait(Library.ImportAndBackup.Restore.CHOOSE_FILE, 10)
            logger.debug('Choose File option is present on the page.')
            click(Library.ImportAndBackup.Restore.CHOOSE_FILE)
        except FindError:
            raise FindError('Choose File option is NOT present on the page, aborting.')

    @staticmethod
    def browse_files(file_type, file_name):

        try:
            wait(BrowseWindow.FILE_TYPE_OPTIONS, 10)
            logger.debug('Options button is present on the page.')
            click(BrowseWindow.FILE_TYPE_OPTIONS)
        except FindError:
            raise FindError('Options button is NOT present on the page, aborting.')

        try:
            wait(BrowseWindow.FILE_TYPE_LIST, 10)
            logger.debug('List of file type options is present on the page.')
            click(BrowseWindow.FILE_TYPE_LIST)
        except FindError:
            raise FindError('List of file type options is NOT present on the page, aborting.')

        mouse_move(BrowseWindow.FILE_TYPE_OPTIONS, 1)

        try:
            if file_type == 'JSON':
                wait(BrowseWindow.JSON, 10)
                logger.debug('JSON option is present on the page.')
                click(BrowseWindow.JSON)
            else:
                wait(BrowseWindow.ALL_FILES, 10)
                logger.debug('All Files option is present on the page.')
                click(BrowseWindow.ALL_FILES)
        except FindError:
            raise FindError('Searched file type options are not present on the page, aborting.')

        try:
            wait(BrowseWindow.SEARCH_FIELD, 10)
            logger.debug('Search field is present on the page.')
            click(BrowseWindow.SEARCH_FIELD)
        except FindError:
            raise FindError('Search field is not present ont the page, aborting.')

        paste(file_name)

        try:
            wait(BrowseWindow.BACKUP_FILE, 10)
            logger.debug('Searched backup file is present on the page.')
            click(BrowseWindow.BACKUP_FILE)
        except FindError:
            raise FindError('Searched backup file is NOT present on the page, aborting.')

        try:
            wait(BrowseWindow.OPEN_BUTTON, 10)
            logger.debug('Open button is present on the page.')
            click(BrowseWindow.OPEN_BUTTON)
        except FindError:
            raise FindError('Open button is NOT present on the page, aborting.')

        try:
            wait(BrowseWindow.OK_BUTTON, 10)
            logger.debug('Ok button is present on the page.')
            click(BrowseWindow.OK_BUTTON)
        except FindError:
            raise FindError('Ok button is NOT present on the page, aborting.')
