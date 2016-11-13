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

<p> Created by: Narasimha Prasanna HN</p>
