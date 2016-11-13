from Python import imports as SPEECHLIB_IMPORT_TOOLS
import zipfile
PACKAGE_STRING={"gTTS","nltk", "pyttsx"}
#check network connection before installation
def extract_installer_zip():
  zip=zipfile.ZipFile("Python\\Installer_Zip.zip")
  zip.extractall("Python\\")
def installer_main():
    response=SPEECHLIB_IMPORT_TOOLS.Check_Connection()
    if response:
      print(str(SPEECHLIB_IMPORT_TOOLS.getOSName()))
      print("Network found")
      SPEECHLIB_IMPORT_TOOLS.download_packages_Import(PACKAGE_STRING)
      print("Installed gTTS to Python"+ str(SPEECHLIB_IMPORT_TOOLS.PLATFORM_TOOLS.python_version()))
      file_setFlag=open("Python\\Flag.txt","w")
      file_setFlag.write("1")
      file_setFlag.close()
      print("Creating directories...")
      extract_installer_zip()
    else: print("Check internet connection")
    pass

