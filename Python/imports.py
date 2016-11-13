import os as OPERATING_SYSTEM_TOOLS
import platform as PLATFORM_TOOLS
import pip, importlib, pkgutil, socket

def getOSName():
    osname=PLATFORM_TOOLS.architecture()
    return osname


def download_packages_Import(__PACKAGE_NAME):
    packages=""
    try: 
        for packages in __PACKAGE_NAME:
            pip.main(['install', packages])
    finally:
        print(packages+"installed successfully")
    pass


def run_x64_gTTS_Test(osname, package_name):
    print("Running diagnostics...")
    print(osname)
    pass

def Check_Connection():
    REMOTE_SERVER="www.google.com"
    try:
        host=socket.gethostbyname(REMOTE_SERVER)
        s=socket.create_connection((host,80),2)
        return True
    except: return False

def create_User_Dirs():
    
    OPERATING_SYSTEM_TOOLS.mkdir("Data")
    OPERATING_SYSTEM_TOOLS.mkdir("IO")
    OPERATING_SYSTEM_TOOLS.mkdir("Data\\Speech")
    OPERATING_SYSTEM_TOOLS.mkdir("Data\\mp3")
    OPERATING_SYSTEM_TOOLS.mkdir("IO\\temp")

