import json


def loadEventData():
    file = open("data/event.json")
    data = json.load(file)
    return data

def printEvent(data):
    print("#"*30)
    print(f"Event: {data['title']}")
    print(f"Date: {data['date']}")
    print(f"Guests: {len(data['guests'])}")
    print("#"*30)
    
def inviteGuest(data):
    name = input("Enter guest name: ")
    data["guests"].append(name)
    return data

def saveData(data):
    file = open("data/event.json","w")
    json.dump(data,file)
    file.close()

def menu(title,options):
    print(f"##### {title:^15} #####")
    for k in options:
        print(f"{k}  {options[k]}")
    print(f"##### {'Choose the option':^15} #####")

    selected = int(input(">> "))
    if selected not in options:
        print("Wrong option!!!")
    return selected

def pquestslist(data):
    print("#"*30)
    print(f"Guests: {data['guests']}")
    print("#"*30)

def delquest(data):
    name = input("Enter existing quest: ")
    data["guests"].remove(name)
    return data

        
        
        
        
        
        
        
#print(f"ERROR: the term '{term}' DOES NOT exist!")

#fiecare invitat sa aiba nr lui,dupa care il vom putea sterge,sau schimba numele