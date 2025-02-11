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

from settings import *

"""Still semi under refinement but functional, like card entry, this function uses the GUI results to
search through the save file for cards that match ans displays the data back in a scrollable window.
Depending on your entered query you can return the exact card or several cards."""

def cardSearch():
    while True:
        searchForm = [
            [gui.Text("Please enter search value(s): (not all are required & name is case sensitive)")],
            [gui.Text("Card Name", size=(15,1)), gui.InputText()],     # value[0]
            [gui.Text("Super Type(s)")],
            [gui.Checkbox('Land', default=False)],                        # value[1]
            [gui.Checkbox('Creature', default=False)],                    # value[2]
            [gui.Checkbox('Legendary', default=False)],                   # value[3]
            [gui.Checkbox('Planeswalker', default=False)],                # value[4]
            [gui.Checkbox('Artifact', default=False)],                    # value[5]
            [gui.Checkbox('Enchantment', default=False)],                 # value[6]
            [gui.Checkbox('Instant', default=False)],                     # value[7]
            [gui.Checkbox('Sorcery', default=False)],                     # value[8]
            [gui.Checkbox('Battle', default=False)],                      # value[9]
            [gui.Text("Mana Cost", size=(15,1)), gui.InputText()],       # value[10]
            [gui.Text("Power", size=(15,1)), gui.InputText()],           # value[11]
            [gui.Text("Toughness", size=(15,1)), gui.InputText()],       # value[12]
            [gui.Button("Search")],
            [gui.Button("Close")]]
        
        window = gui.Window("MTG Card Search", searchForm)
        windowEvent, windowValues = window.read()

        if windowEvent == "Close" or windowEvent == gui.WIN_CLOSED:
            window.close()
            del window
            break

        while True:
            if windowEvent == "Search":
                cardFile = []
                with open(file.filepath, 'r') as database:
                    for line in database:
                        line = line.rstrip()
                        subdata = eval(line)
                        cardFile.append(subdata)
                    database.close()
    
            searchList = []

            for card in cardFile:
                if windowValues[0] != '':   #Name
                    if card['Name'] not in searchList and card['Name'] == windowValues[0]:
                        searchList.append(card['Name'])

                if windowValues[1] == True: #Land
                    if card['Name'] not in searchList and card['Super Type'] == windowValues[1]:
                        searchList.append(card['Name'])
                if windowValues[2] == True: #Creature
                    if card['Name'] not in searchList and card['Super Type'] == windowValues[2]:
                        searchList.append(card['Name'])
                if windowValues[3] == True: #Legendary
                    if card['Name'] not in searchList and card['Super Type'] == windowValues[3]:
                        searchList.append(card['Name'])
                if windowValues[4] == True: #Planeswalker
                    if card['Name'] not in searchList and card['Super Type'] == windowValues[4]:
                        searchList.append(card['Name'])
                if windowValues[5] == True: #Artifact
                    if card['Name'] not in searchList and card['Super Type'] == windowValues[5]:
                        searchList.append(card['Name'])
                if windowValues[6] == True: #Enchantment
                    if card['Name'] not in searchList and card['Super Type'] == windowValues[6]:
                        searchList.append(card['Name'])
                if windowValues[7] == True: #Instant
                    if card['Name'] not in searchList and card['Super Type'] == windowValues[7]:
                        searchList.append(card['Name'])
                if windowValues[8] == True: #Sorcery
                    if card['Name'] not in searchList and card['Super Type'] == windowValues[8]:
                        searchList.append(card['Name'])
                if windowValues[9] == True: #Battle
                    if card['Name'] not in searchList and card['Super Type'] == windowValues[9]:
                        searchList.append(card['Name'])

                if windowValues[10] != '': #Mana
                    if card['Name'] not in searchList and card['Mana'] == windowValues[10]:
                        searchList.append(card['Name'])
                if windowValues[11] != '': #Power
                    if card['Name'] not in searchList and card['Power'] == windowValues[11]:
                        searchList.append(card['Name'])
                if windowValues[12] != '': #Toughness
                    if card['Name'] not in searchList and card['Tough'] == windowValues[12]:
                        searchList.append(card['Name'])

            if searchList == []:
                error.display_error(6)
                window.close()
                del window
                break
            else:
                results = ''
                for card in searchList:
                    with open(file.filepath, 'r') as database:
                        for line in database:
                            line = line.rstrip()
                            subdata = eval(line)
                            if card == subdata['Name']:
                                subResults = (f"""Name: {subdata['Name']}\nColor: {subdata['Color']}\nSuper Type: {subdata['Super Type']}\nSub Type: {subdata['Sub Type']}\nMana: {subdata['Mana']}\nPower: {subdata['Power']}\nToughness: {subdata['Toughness']}\nAbility Text: {subdata['Ability Text']}\nDuplicates: {subdata['Duplicates']}\n~~~~~~~~~~~~~~\n""")
                        database.close()
                        results += subResults 
                window.close()
                del window

                column1 = [
                    [gui.Text(results)]
                ]
                layout = [[gui.Column(column1, size=(150,150), scrollable=True, vertical_scroll_only=True)]]
                resultsWindow = gui.Window('Search Results', layout)
                resultsWindowEvent, resultsWindowValues = resultsWindow.read()
                resultsWindow.close()
                break

#Un-comment when testing this file
#cardSearch()