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

try:
    import PySimpleGUI as gui
    gui.theme("DarkPurple1")
except:
    ImportError
    print("Run `python3 -m pip install pysimplegui` & try again.")
    
from files import file
from card_entry import cardEntry
from card_search_2 import cardSearch

def mainProgramLoop():
    while True:
#Main Menu Screen
        mainMenu = [
            [gui.Text("This is the MTG Card Collector!")],
            [gui.Column([[gui.Button("Card Entry", size=(10, 1))]], justification="center")],
            [gui.Column([[gui.Button("Search Cards", size=(10, 1))]], justification="center")],
            [gui.Column([[gui.Button("Help", size=(10, 1))]], justification="center")],
            [gui.Column([[gui.Button("Exit", size=(10, 1))]], justification="center")],
            [gui.Text("This program was created by:\n\tQuira Walker\nSpecial credit goes to:\n\tMissCthuleanCoder\nCredit also to:\n\tMembers of several Discord Servers &\n\tQuira's friends who have all helped in\n\tthe creation of this program.\n\nHad it not been for the help of these amazing people,\nthis project never would have been made possible.\nA deep most sincere, Thank You.")]
        ]

        file.run_check()

        menu = gui.Window("Welcome", mainMenu)
        menuEvent, menuValues = menu.read()
#Card Entry Button / Error
        if menuEvent == "Card Entry":
            menu.close()
            del menu
            try:
                cardEntry()
            except:
                error3 = gui.popup_ok("There seems to be an error running this function, please try again. If the issue persists please make note of the error code and contact the creator.", title="Error: 3")
#Card Search Button / Error
        if menuEvent == "Search Cards":
            menu.close()
            del menu
            try:
                cardSearch()
            except:
                error4 = gui.popup_ok("There seems to be an error running this function, please try again. If the issue persists please make note of the error code and contact the creator.", title="Error: 4")
#Help Button
        if menuEvent == "Help":
            menu.close()
            del menu
            helpMenu = gui.popup_ok("Card Entry: This function lets you enter cards to be saved.\nSearch: This function allows you to search previously entered cards..\nHelp: This current Menu.\nExit: Exits and closes the program.",title="Help Menu")
#Exit Button
        if menuEvent == "Exit" or menuEvent == gui.WINDOW_CLOSED:
            break
        
    menu.close()

if __name__ == '__main__':
    mainProgramLoop()