## Unarchiver - Simple .rar/.zip extraction script for XBMC4Xbox.

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import xbmcvfs
import os

def select_file_dialog(title, filetypes):
    dialog = xbmcgui.Dialog()
    file = dialog.browse(1, title, 'files', filetypes)
    return file

def select_folder_dialog(title):
    dialog = xbmcgui.Dialog()
    folder = dialog.browse(0, title, 'files')
    return folder

def extract_archive_to_dest(archive_file, dest_folder):
    if not xbmcvfs.exists(dest_folder):
        xbmcvfs.mkdirs(dest_folder)
    
    xbmc.executebuiltin('XBMC.Extract("%s", "%s")' % (archive_file, dest_folder))

def main():
    archive_file = select_file_dialog("Select archive file", "*.rar|*.zip")
    if not archive_file:
        xbmcgui.Dialog().ok("Error", "No archive file selected.")
        return
    
    dest_folder = select_folder_dialog("Select destination folder")
    if not dest_folder:
        xbmcgui.Dialog().ok("Error", "No destination folder selected.")
        return
    
    extract_archive_to_dest(archive_file, dest_folder)
    xbmcgui.Dialog().ok("Success", "Files extracted successfully!")

if __name__ == '__main__':
    main()
