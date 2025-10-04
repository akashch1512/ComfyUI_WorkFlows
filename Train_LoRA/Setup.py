import os
from Tools.unzip import unzip_file
from Download.Realviz import Install_Realviz
from time import sleep

print("================================")
print("Starting Setup...")
print("================================")

os.chdir("/workspace/")

os.system("git clone https://github.com/bmaltais/kohya_ss")

os.chdir("/workspace/kohya_ss/sd-scripts")

os.system("git submodule init")

os.system("git submodule update")

os.system('gdown "https://drive.google.com/uc?id=1ybTkd0d_XOazmk9B1VFxCRJHZXzLUDpp"')

sleep(2)

unzip_file()

Install_Realviz()

print("===============================")
print("Setup Completed Successfully!")
print("===============================")