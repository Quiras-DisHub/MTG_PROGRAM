'''
    MTG Card Manager (A simple GUI program to log your MTG cards and the search for cards to see if you have them or not.)
    Copyright (C) 2024  Quira Walker

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import time, os
import PySimpleGUI as gui

gui.theme("DarkPurple1")
"""This class hold the main file functions required throughout the program from
verifying folder/file precence to saving data it is all handled by these functions
This is written for both Linux and Windows file systems"""
class Files():
    def __init__(self):
        self.catalogue = "mtg_card_catalogue.txt"
        self.directory = "/home/master/MTG_PROGRAM/MTG"
        self.filepath = os.path.join(self.directory, self.catalogue)
#Checks for the save folder and creates if does not exist yet
    def check_for_folder(self):
        if not os.path.exists(self.directory):
            error1 = gui.popup_no_buttons(f"The {self.directory} folder does not exist. Creating the folder now...", title="Error: 1", auto_close=True, auto_close_duration=5)
            os.makedirs(self.directory)
#checks for the save file and creates if does not exist in the above folder
    def check_for_file(self):
        if not os.path.exists(self.filepath):
            error2 = gui.popup_no_buttons(f"The {self.catalogue} file does not exist at {self.directory}. Creating the file now...", title="Error: 2", auto_close=True, auto_close_duration=5)
            open(self.filepath, 'w').close()
#saves your cards as they are entered allowing for later recall in the search and future functions
    def save_file(self, data):
        with open(self.filepath, 'a') as database:
            database.write(str(data) + "\n")
            database.close()

    def run_check(self):
        file.check_for_folder()
        time.sleep(0.125)
        file.check_for_file()
        time.sleep(0.125)

file = Files()