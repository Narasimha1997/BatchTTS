from Python import install
__CALL_FILE_PATH="IO\\__CALL.txt"
from Python import imports as PACKAGE_TOOLS
def handle_calls(__CALL_STRING):
    if __CALL_STRING=="run tests":
        oSystem=PACKAGE_TOOLS.getOSName()
        PACKAGE_TOOLS.run_x64_gTTS_Test(oSystem, "gTTS")
    if __CALL_STRING=="run gtts":
        Speech_Engine.gTTS_Core('en')

    pass
def call_api():
   flag=open("Python\\Flag.txt", "r")
   flag_data=flag.read()
   if flag_data=="1":
      from Python.Installer_Zip import Speech_Engine

      CALL=open(__CALL_FILE_PATH,"r")
      handle_calls(CALL.read())
   else: install.installer_main()
#This API is used to interact Speech_Engine with External tools
#Can be called by JavaScript, php or Node.js

