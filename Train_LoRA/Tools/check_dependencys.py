import importlib

def check_dependencies():
    print("Checking Dependencies...")
    
    libs_to_check = [
        # Hugging Face core
        "torch", "torchvision", "torchaudio",
        "transformers", "diffusers", "accelerate",

        # Memory/optimization
        "xformers", "bitsandbytes", "safetensors", "einops",

        # Training frameworks
        "pytorch_lightning", "prodigyopt", "lion_pytorch",

        # Data & preprocessing
        "opencv-python", "cv2", "PIL", "ftfy", "sentencepiece", "datasets",

        # Utils & viz
        "tensorboard", "huggingface_hub", "altair", "easygui",
        "toml", "voluptuous", "imagesize", "rich"
    ]

    # special cases where version attribute differs
    special_version_attrs = {
        "cv2": "version",
        "PIL": "PILLOW_VERSION",  # old
    }

    for lib in libs_to_check:
        try:
            module_name = lib.replace("-", "_")
            module = importlib.import_module(module_name)

            # try __version__, or special attributes, or unknown
            version = getattr(module, "__version__", None)
            if version is None:
                # handle cv2, PIL, etc.
                if lib in special_version_attrs:
                    version = getattr(module, special_version_attrs[lib], None)
                elif lib == "PIL":
                    try:
                        import PIL
                        version = getattr(PIL, "__version__", None)
                    except Exception:
                        version = None

            print(f"✅ {lib} - {version if version else 'unknown'}")

        except Exception as e:
            print(f"❌ {lib} - MISSING ({e.__class__.__name__})")