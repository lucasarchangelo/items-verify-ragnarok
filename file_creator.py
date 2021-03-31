def createFile(fileName, listItems, fileType):
    f = open(fileName, "a")
    f.write("Id;ResourceName;Name;HasBmpCollection;HasBmpItem;HasAct\n")
    if fileType == "server":
        for item in listItems:
            f.write(str(item) +";;;;;;\n")
    if fileType == "client":
        for item in listItems:
            f.write(item.idName + ";" + item.identifiedResourceName +";" + item.identifiedDisplayName +";;;;\n")
    if fileType == "itemFound":
         for item in listItems:
            f.write(item.idName + ";" + item.identifiedResourceName  + ";" + item.identifiedDisplayName 
                 + ";" + item.hasBmpCollection  + ";" + item.hasBmpItem  + ";" + item.hasActSpr +"\n")
    f.close()