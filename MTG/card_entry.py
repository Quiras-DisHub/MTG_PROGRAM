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
from files import file

"""This is the card search function that reads the results of the GUI window and saves
the subsequntly made dictionary for each card. If it detects a duplicate card the
card_dict['Duplicates'] is incremented by 1 for that card"""

def cardEntry():
    while True:
        entryForm = [
            [gui.Text("Card Name:", size=(15, 1)), gui.InputText()],      # value[0]
            [gui.Text("Please Select Color(s)")],
            [gui.Checkbox('Colorless', default=False)],                   # value[1]
            [gui.Checkbox('Black', default=False)],                       # value[2]
            [gui.Checkbox('White', default=False)],                       # value[3]
            [gui.Checkbox('Green', default=False)],                       # value[4]
            [gui.Checkbox('Blue', default=False)],                        # value[5]
            [gui.Checkbox('Red', default=False)],                         # value[6]
            [gui.Text("Please Select Super Type(s)")],
            [gui.Checkbox('Land', default=False)],                        # value[7]
            [gui.Checkbox('Creature', default=False)],                    # value[8]
            [gui.Checkbox('Legendary', default=False)],                   # value[9]
            [gui.Checkbox('Planeswalker', default=False)],                # value[10]
            [gui.Checkbox('Artifact', default=False)],                    # value[11]
            [gui.Checkbox('Enchantment', default=False)],                 # value[12]
            [gui.Checkbox('Instant', default=False)],                     # value[13]
            [gui.Checkbox('Sorcery', default=False)],                     # value[14]
            [gui.Checkbox('Battle', default=False)],                      # value[15]
            [gui.Text("Sub Type:", size=(15, 1)), gui.InputText()],       # value[16]
            [gui.Text("Mana Cost:", size=(15, 1)), gui.InputText()],      # value[17]
            [gui.Text("Power:", size=(15, 1)), gui.InputText()],          # value[18]
            [gui.Text("Toughness:", size=(15, 1)), gui.InputText()],      # value[19]
            [gui.Text("Ability Text:", size=(15, 1)), gui.InputText()],   # value[20]
            [gui.Button("Verify")],
            [gui.Button("Close")]]
        
        window = gui.Window("MTG Card Entry", entryForm)
        event, values = window.read()

        if event == "Close" or event == gui.WIN_CLOSED:
            window.close()
            del window
            break

        card_dict = {'Name' : '', 'Color' : '', 'Super Type' : '', 'Sub Type' : '', 'Mana' : '', 'Power' : '', 'Toughness' : '', 'Ability Text' : '', 'Duplicates' : 0}

        color_string = []
        if values[1] is True:
            color_string.append('Colorless')
            values[2] = False
            values[3] = False
            values[4] = False
            values[5] = False
            values[6] = False
        if values[2] is True:
            color_string.append('Black')
        if values[3] is True:
            color_string.append('White')
        if values[4] is True:
            color_string.append('Green')
        if values[5] is True:
            color_string.append('Blue')
        if values[6]is True:
            color_string.append('Red')

        super_string = []
        if values[7] is True:
            super_string.append('Land')
        if values[8] is True:
            super_string.append('Creature')
        if values[9] is True:
            super_string.append('Legendary')
        if values[10] is True:
            super_string.append('Planeswalker')
        if values[11] is True:
            super_string.append('Artifact')
        if values[12] is True:
            super_string.append('Enchantment')
        if values[13] is True:
            super_string.append('Instant')
        if values[14] is True:
            super_string.append('Sorcery')
        if values[15] is True:
            super_string.append('Battle')

        if values[16] != '':
            subType_choice = values[16]
        else:
            subType_choice = 'N/A'
        if values[17] != '':
            mana_choice = values[17]
        else:
            mana_choice = 'N/A'
        if values[18] != '':
            power_choice = values[18]
        else:
            power_choice = 'N/A'
        if values[19] != '':
            toughness_choice = values[19]
        else:
            toughness_choice = 'N/A'
        if values[20] != '':
            ability_choice = values[20]
        else:
            ability_choice = 'N/A'

        cardName = values[0]
        card_dict['Name'] = cardName
        card_dict['Color'] = color_string
        card_dict['Super Type'] = super_string
        card_dict['Sub Type'] = subType_choice
        card_dict['Mana'] = mana_choice
        card_dict['Power'] = power_choice
        card_dict['Toughness'] = toughness_choice
        card_dict['Ability Text'] = ability_choice
            
        verification = f"Card Name: {cardName}\nCard Color(s): {color_string}\nSuper Type: {super_string}\nSub Type: {subType_choice}\nMana Cost: {mana_choice}\nPower: {power_choice}\nToughness: {toughness_choice}\nAbility Text: {ability_choice}"
    
        while True:
            if event == "Verify":
                verify = gui.popup_yes_no(f"Please confirm everything is correct:\n{verification}", title="Verification")
                if verify == "Yes":
                    CARDS = []
                    with open(file.filepath, 'r') as database:
                        for line in database:
                            line = line.rstrip()
                            subdata = eval(line)
                            CARDS.append(subdata)
                        database.close()
                    os.remove(file.catalogue)

                    if CARDS == []:
                        file.save_file(card_dict)
                    trackMT = False
                    MT = False
                    for card in CARDS:
                        if cardName == card['Name']:
                            duplicates = card['Duplicates']
                            duplicates += 1
                            card['Duplicates'] = duplicates
                            file.save_file(card)
                            trackMT = True
                        elif cardName != card['Name']:
                            file.save_file(card)
                            MT = True
                        if trackMT is False and MT is True:
                            file.save_file(card_dict)
                        MT = False

                    window.close()
                    del window
                    break
                elif verify == "No":
                    window.close()
                    verify = gui.popup_no_buttons("Please re-enter your card", title="Verify Failed", auto_close=True, auto_close_duration=2)
                    del window
                    break
                elif verify == gui.WINDOW_CLOSED:
                    window.close()
                    del window
                    break
                
#Un-comment when testing this file
#cardEntry()