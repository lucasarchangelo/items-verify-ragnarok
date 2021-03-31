import configparser

def formatId(luaLine):
    return luaLine.replace("[", "").replace("]", "").replace(" = {", "").strip()

def formatResourceName(luaLine):
    return luaLine.replace("identifiedResourceName = \"", "").replace("\",", "").strip()

def formatDisplayName(luaLine):
    return luaLine.replace("identifiedDisplayName = \"", "").replace("\",", "").strip()

class ItemLua:
    def __init__(self, *args):
        if len(args) == 3:
            self.idName = args[0]
            self.identifiedResourceName = args[1]
            self.identifiedDisplayName = args[2]
        if len(args) > 3:
            self.idName = args[0]
            self.identifiedResourceName = args[1]
            self.identifiedDisplayName = args[2]
            self.hasBmpItem = args[3]  
            self.hasBmpCollection = args[4]
            self.hasActSpr = args[5]

def fatory_lua():
    config = configparser.ConfigParser()
    config.read_file(open("paths.conf"))
    luaObjectsList = []
    flua = open(config['DEFAULT']['LuaFile'], "r")
    itemLua = ItemLua()
    for line in flua:
        if "] = {" in line: 
            itemLua.idName = formatId(line)
        if "unidentifiedDisplayName" not in line and "identifiedDisplayName" in line:
            itemLua.identifiedDisplayName = formatDisplayName(line)
        if "unidentifiedResourceName" not in line and "identifiedResourceName" in line:
            itemLua.identifiedResourceName = formatResourceName(line)
            luaObjectsList.append(ItemLua(itemLua.idName, itemLua.identifiedResourceName, itemLua.identifiedDisplayName))
    # for item in luaObjectsList:
        # print(item.idName, item.identifiedResourceName)
    flua.close()
    return luaObjectsList

