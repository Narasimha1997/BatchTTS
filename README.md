# BatchTTS
A batch Text-to-Speech conversion over text from multiple text files.
<h1>BatchTTS</h1>
<p>A free TTS tool based on Google TTS engine, The project is designed to accept multiple Text files together and produce individual
.mp3 files for that corresponding text file</p>
<p>The Project can also be used as a library for large applications which uses TTS batch processing over multiple files as a part of it
Use API.py as an interface to interact with the inbuilt speech engine using gTTS</p>

<p>The library contains an inbuilt package downloader using pip and an automated Setup which configures the libray for use, It is just
a one time installation, Just import API.py. API.py automatically checks the internet connection and gTTS package, if it isn't installed
gTTS will be downloaded automatically and configured, Once gTTS is successfully installed, The Installer_Zip.zip will be automatically
installed in its prescribed directory and configured automatically. </p>

<h2>Requirements:</h2>
<p> Python 3.5+ </p>
<p> BatchTTS uses PIP to download gTTS if its not present, if it fails, Download gTTS manually and configure it</p>
<p> If installer fails to install Install_Zip.zip file, Then manually extract it inside Python directory </p>
<p> Working internet connection for installation and to interact with Google TTS engine</p>
<h3>Important Note:</h3>
<p>Remove .gitkeep files from mp3 and Data directories before using it </p>

<h4>How to use: </h4>
<p> Clone the project and run API.py file, It automatiaclly checks the installation for the first time and downloads the required packages
Remove .gitkeep files from Data and mp3 folders and now you are ready to go</p>
<p> Place the .txt files you need to convert into Data directory, it can be any no. of files, Now launch API.py to convert Text to speech
and the generated output will be placed automatically inside mp3 directory.</p>
<h5>Using BatchTTS as Library</h5>
<p>Clone the project and Modify the API.py to use it as a library</p>
<p> Use from BatchTTS import API to use API
<p> Your application should place the .txt files inside Data folder programatically then it should call API.py to use TTS</p>
<h6> Disabling the library </h6>
<p> You can notice __CALLS.txt inside IO Directory the content is run gtts by default, Remove it and leave the file empty </p>
<p> Created by: Narasimha Prasanna HN</p>
