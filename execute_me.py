import yaml
import luadata
import configparser

from lua_factory import fatory_lua
from file_creator import createFile
from files_verify import verifyFiles

config = configparser.ConfigParser()
config.read_file(open("paths.conf"))

with open(r'' + config['DEFAULT']['YmlFile']) as file:
    item_db_equip = yaml.full_load(file)
    data = fatory_lua()
    listServerHasClientNot = []
    clientHasServerNot = []
    clientAndServerHas = []
    for item in item_db_equip['Body']:
        found = False
        for objectLua in data:
            if item['Id'] == objectLua.idName:
                found = True
                break
        if found == False:
            listServerHasClientNot.append(item['Id'])
    
    for objectLua in data:
        found = False
        for item in item_db_equip['Body']:
            if item['Id'] == int(objectLua.idName):
                found = True
                config_items = verifyFiles(objectLua.identifiedResourceName)
                objectLua.hasActSpr = config_items['verifyFilesActSpr']
                objectLua.hasBmpCollection = config_items['verifyFilesCollectionBMP']
                objectLua.hasBmpItem = config_items['verifyFilesItemBMP']
                clientAndServerHas.append(objectLua)
                break
        if found == False:
            clientHasServerNot.append(objectLua)

    print("Server Has But Client Not")
    createFile("Server_Has_But_Client_Not.csv", listServerHasClientNot, "server")

    print("Client Has But Server Not")
    createFile("Client_Has_But_Server_Not.csv", clientHasServerNot, "client")
    
    print("Client and Server Has")
    createFile("Client_And_Server_Has.csv", clientAndServerHas, "itemFound")
    