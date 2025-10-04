import os
from Tools.unzip import unzip_file

os.chdir("/workspace/")

os.system('gdown "https://drive.google.com/uc?id=1ybTkd0d_XOazmk9B1VFxCRJHZXzLUDpp"')

unzip_file("Navya_LoRA_3000.zip", "/workspace/LoRA/LoRA_Output/Navya/")

print("✅ Resume setup completed!")