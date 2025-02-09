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
try:
    import PySimpleGUI as gui
except ImportError:
    print("Run `python3 -m pip install pysimplegui` & try again.")
from files import file
from card_entry import cardEntry
from card_search_2 import cardSearch


#GUI Settings
gui.theme('DarkBrown2') #See the GUI_THEME.png file if you wish to use a different GUI

#Errors
class Errors:
    def __init__(self):
        self.errorPersists      = "If this issue persists please make note of the error code found in the title bar and contact the creator."
        self.saveError1         = f"The containing folder does not exist. Creating the folder now..."
        self.saveError2         = f"The save file does not exist in the folder. Creating the file now..."
        self.saveError3         = "An error has occured during the save, please try again."
        self.mainFunctionError4 = "Card Entry function error, please try again."
        self.mainFunctionError5 = "Card Search function error, please try again."
        self.searchError6       = "No cards could be found."
        self.errorList          = ['0',self.saveError1,self.saveError2,self.saveError3,self.mainFunctionError4,self.mainFunctionError5,self.searchError6]
    def display_error(self, number, auto=False):
        if auto == True:
            return gui.popup_no_buttons(self.errorList[number], title=f'Error: {number}', auto_close=True, auto_close_duration=5)
        return gui.popup_ok(f'{self.errorList[number]}\n{self.errorPersists}', title=f'Error: {number}')
error = Errors()