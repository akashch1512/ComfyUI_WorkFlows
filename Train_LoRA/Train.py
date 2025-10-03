from Tools.check_dependencys import check_dependencies
from Tools.makedir import makedir
import os

print("====================================")
print("🚀 LoRA Training with Realviz XL 5.0")
print("Checking Dependencies...")
print("====================================")

check_dependencies()

print("====================================")
print("🚀 Setting up directories...")
print("====================================")

DATASET_DIR, OUTPUT_DIR, LOG_DIR = makedir()

print("====================================")
print("Training Configuration")
print("====================================")


PRETRAINED_MODEL = "/workspace/RealVisXL_V5.0"


RESOLUTION      = 1024
BATCH_SIZE      = 2
GRAD_ACC_STEPS  = 4
MAX_STEPS       = 3000         # i can resume the training later but will train till 3000 steps then test again and will start again
NETWORK_DIM     = 128
NETWORK_ALPHA   = 128
LEARNING_RATE   = 1.0

# ----------------------
# TRAINING COMMAND
# ----------------------

train_cmd = f'''
accelerate launch --mixed_precision=bf16 /workspace/kohya_ss/sd-scripts/sdxl_train_network.py \\
  --pretrained_model_name_or_path="{PRETRAINED_MODEL}" \\
  --train_data_dir="{DATASET_DIR}" \\
  --output_dir="{OUTPUT_DIR}" \\
  --logging_dir="{LOG_DIR}" \\
  --resolution={RESOLUTION} \\
  --network_module=networks.lora \\
  --network_dim={NETWORK_DIM} \\
  --network_alpha={NETWORK_ALPHA} \\
  --learning_rate={LEARNING_RATE} \\
  --train_batch_size={BATCH_SIZE} \\
  --gradient_accumulation_steps={GRAD_ACC_STEPS} \\
  --max_train_steps={MAX_STEPS} \\
  --save_every_n_steps=500 \\
  --save_last_n_steps=3 \\
  --save_last_n_epochs=3 \\
  --save_state \\
  --save_precision=bf16 \\
  --optimizer_type=Prodigy \\
  --mem_eff_attn \\
  --caption_extension=.txt \\
  --max_data_loader_n_workers=4 \\
  --log_prefix="LoRA_Logs" \\
  --enable_bucket \\
  --bucket_reso_steps=64 \\
  --log_with tensorboard \\
  2>&1 | tee /workspace/train.log
'''

print("====================================")
print("🚀 Starting Training...")
print("====================================")

print("🚀 Resuming LoRA training with Colab Pro A100/L4...\n")
exit_code = os.system(train_cmd)
print("\n✅ Training finished with exit code:", exit_code)

