import os
from Tools.unzip import unzip_file
from Install.Realviz import Install_Realviz

"""pip install huggingface-hub==0.35.0"""

os.system("git clone https://github.com/bmaltais/kohya_ss")

os.changecwd("/workspace/kohya_ss/sd-scripts")

os.system("git submodule init")

os.system("git submodule update")

os.system("pip install --upgrade gdown")

os.system("pip install hf_transfer")

os.system('gdown "https://drive.google.com/uc?id=1ybTkd0d_XOazmk9B1VFxCRJHZXzLUDpp"')

unzip_file()

Install_Realviz()