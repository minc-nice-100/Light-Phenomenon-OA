# -*- coding: utf-8 -*-
print("Hello, World!")
print("""
---------------------
  _     _       _     _   ____       _                                                             ___    _    
 | |   (_) __ _| |__ | |_|  _ \     | |__   ___ _ __   ___  _ __ ___   ___ _ __   ___  _ __       / _ \  / \   
 | |   | |/ _` | '_ \| __| |_) |    | '_ \ / _ | '_ \ / _ \| '_ ` _ \ / _ | '_ \ / _ \| '_ \     | | | |/ _ \  
 | |___| | (_| | | | | |_|  __/     | | | |  __| | | | (_) | | | | | |  __| | | | (_) | | | |    | |_| / ___ \ 
 |_____|_|\__, |_| |_|\__|_|        |_| |_|\___|_| |_|\___/|_| |_| |_|\___|_| |_|\___/|_| |_|     \___/_/   \_\\
           |___/                                                                                                                                                                                                        
---------------------
      """)
import os
import django

print("Django version:", django.get_version())
print("Python version:", os.sys.version)
print("Current working directory:", os.getcwd())
print("Current user:", os.getlogin())
