from app import loadEventData
from app import printEvent
from app import inviteGuest
from app import saveData
from app import menu
from app import pquestslist
from app import delquest
##########################################
while True:
    result = menu("MENU", {
        0: "Exit",
        1: "Invite",
        2: "Displays the guest list",
        3: "Delete the guest from the list"
    })
    
    if result == 1:
        data = loadEventData()
        data = inviteGuest(data)
        saveData(data)

    if result == 2:
        data = loadEventData()
        pquestslist(data)

    if result == 3:
        data = loadEventData()
        delquest(data)
        saveData(data)

    if result == 0:
            print(" Thank you! ")
            break




        
        