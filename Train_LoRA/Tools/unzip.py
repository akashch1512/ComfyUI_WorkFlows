import zipfile

def unzip_file(zip_path="/workspace/Navya.zip", extract_to="/workspace/LoRA/Navya/2_Navya"):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

