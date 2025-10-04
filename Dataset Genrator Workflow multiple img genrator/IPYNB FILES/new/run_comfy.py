import os
import subprocess

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

# Step 1: cd /workspace/
os.chdir("/workspace")

# Step 2: Clone ComfyUI only if not already present
if not os.path.exists("ComfyUI"):
    run("git clone https://github.com/comfyanonymous/ComfyUI")
else:
    print("ComfyUI already exists, skipping clone.")

# Step 3: cd into custom_nodes
os.chdir("/workspace/ComfyUI/custom_nodes/")

# Step 4: Clone ComfyUI-Manager only if not already present
if not os.path.exists("ComfyUI-Manager"):
    run("git clone https://github.com/Comfy-Org/ComfyUI-Manager")
else:
    print("ComfyUI-Manager already exists, skipping clone.")

# Step 5: Install ComfyUI-Manager requirements
os.chdir("/workspace/ComfyUI/custom_nodes/ComfyUI-Manager/")
run("pip install -r requirements.txt")

# Step 6: Install ComfyUI requirements
os.chdir("/workspace/ComfyUI/")
run("pip install -r requirements.txt")

# Step 7: Run ComfyUI
subprocess.Popen("python3 main.py --listen 0.0.0.0 --port 3000 --fast", shell=True)

print("✅ ComfyUI server started on port 3000")
