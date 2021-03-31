import os.path
import configparser

config = configparser.ConfigParser()
config.read_file(open("paths.conf"))
GRF_ROOT = config['DEFAULT']['GrfRoot'] # "D:/Ragnarok/Ragnarok Server/python-tools/grfs/Mygrf/data/"
ITEM_BMP_PATH = GRF_ROOT + "texture/À¯ÀúÀÎÅÍÆäÀÌ½º/item/"
ACT_SPR_PATH = GRF_ROOT + "sprite/¾ÆÀÌÅÛ/"
COLLECTION_BMP_PATH = GRF_ROOT + "texture/À¯ÀúÀÎÅÍÆäÀÌ½º/collection/"

ACT_SPR_MALE = GRF_ROOT + "sprite/¾Ç¼¼»ç¸®/¿©/¿©_"
ACT_SPR_FEMALE = GRF_ROOT + "sprite/¾Ç¼¼»ç¸®/³²/³²_"

def verifyFiles(strName):
    filesConfigurator = dict()
    filesConfigurator['verifyFilesItemBMP'] = "False"
    filesConfigurator['verifyFilesCollectionBMP'] = "False"
    filesConfigurator['verifyFilesActSpr'] = "False"

    if os.path.isfile(ITEM_BMP_PATH + strName + ".bmp"):
        filesConfigurator['verifyFilesItemBMP'] = "True"
    if os.path.isfile(COLLECTION_BMP_PATH + strName + ".bmp"):
        filesConfigurator['verifyFilesCollectionBMP'] = "True"
    if os.path.isfile(ACT_SPR_PATH + strName +".act") and os.path.isfile(ACT_SPR_PATH + strName +".spr"): # Find by act / spr on normal folder
        filesConfigurator['verifyFilesActSpr'] = "True"
    elif os.path.isfile(ACT_SPR_MALE + strName +".act") and os.path.isfile(ACT_SPR_MALE + strName +".spr"): # Find by act / spr on Male folder
        filesConfigurator['verifyFilesActSpr'] = "True"
    elif os.path.isfile(ACT_SPR_FEMALE + strName +".act") and os.path.isfile(ACT_SPR_FEMALE + strName +".spr"): # Find by act / spr on Female folder
        filesConfigurator['verifyFilesActSpr'] = "True"
    return filesConfigurator
