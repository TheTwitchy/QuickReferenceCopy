# Everything in here is heavily borrowed from https://github.com/theskyliner/CopyFilepathWithLineNumbers/blob/master/CopyFilepathWithLineNumbers.py, which this projects attempts to emulate, and which is it's inspiration. Just needed a couple of changes for my own purposes.

import sublime, sublime_plugin
import datetime
import shutil
import os.path


def getLines(self):
    (rowStart, colStart) = self.view.rowcol(self.view.sel()[0].begin())
    (rowEnd, colEnd)     = self.view.rowcol(self.view.sel()[0].end())

    lines = (str) (rowStart + 1)

    if rowStart != rowEnd:
        #multiple selection
        lines += "-" + (str) (rowEnd + 1)

    return lines


# class ThetwitchyTest01Command(sublime_plugin.TextCommand):
#     def run(self, edit):
#         filename = self.view.file_name()

#         if len(filename) > 0:
#             sublime.set_clipboard(filename + ':' + getLines(self))
#             sublime.status_message("Copied path with line")

class QuickReferenceCopyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        if len(filename) > 0:
            # Copy shortest relpath for file compared to open folders
            relativePath = min(
                (
                    os.path.relpath(filename, os.path.dirname(folder))
                    for folder in sublime.active_window().folders()
                ),
                key=len,
            )
            sublime.set_clipboard(relativePath + ':' + getLines(self))
            sublime.status_message("Copied reference to clipboard")
    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)