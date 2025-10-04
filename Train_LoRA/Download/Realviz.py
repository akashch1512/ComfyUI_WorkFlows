from huggingface_hub import snapshot_download

def Install_Realviz(MODEL_DIR = f"/workspace/RealVisXL_V5.0/"):
    print("Installing Realviz Model...")

    snapshot_download(
        repo_id="SG161222/RealVisXL_V5.0",
        local_dir=MODEL_DIR,
        local_dir_use_symlinks=False,
        allow_patterns = [
        "model_index.json",
        "*.json",                     # include any other small JSON configs
        "tokenizer/*", "tokenizer_2/*",
        "text_encoder/*", "text_encoder_2/*",
        "unet/*",
        "vae/*",
        "scheduler/*",               
        "*fp16.safetensors"
    ]

    )

    print("✅ SDXL 1.0 Base download complete at /content/RealVisXL_V5.0/")