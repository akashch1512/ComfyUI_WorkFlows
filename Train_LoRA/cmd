python3 -m venv .venv

source .venv/bin/activate

pip install huggingface-hub==0.35.0 hf_transfer --upgrade gdown

pip install \
    torch torchvision torchaudio \
    transformers==4.56.1 diffusers==0.35.1 accelerate==1.10.1 safetensors==0.6.2 \
    einops==0.8.1 sentencepiece==0.2.1 datasets==4.0.0 tensorboard==2.19.0 \
    huggingface-hub==0.35.0 altair==5.5.0 toml==0.10.2 imagesize==1.4.1 \
    xformers bitsandbytes pytorch-lightning prodigyopt lion-pytorch opencv-python ftfy \
    easygui voluptuous rich \
    --extra-index-url https://download.pytorch.org/whl/cu128 \
    --upgrade

    
apt update && apt install -y libgl1-mesa-glx