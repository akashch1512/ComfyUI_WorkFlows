import os

def makedir(PROJECT_NAME="Navya", TRIGGER="Navya"):
    print("==== USER CONFIG ====")

    # Paths
    DATASET_DIR  = f"/workspace/LoRA/{PROJECT_NAME}/"
    IMAGES_DIR   = f"/workspace/LoRA/{PROJECT_NAME}/2_{TRIGGER}/" # Dataset Later Added
    OUTPUT_DIR   = f"/workspace/LoRA/LoRA_Output/{PROJECT_NAME}"
    LOG_DIR      = f"/workspace/LoRA/LoRA_Logs/{PROJECT_NAME}"

    # Create folders if not exist
    import os
    for p in [DATASET_DIR, OUTPUT_DIR, LOG_DIR, IMAGES_DIR]:
        os.makedirs(p, exist_ok=True)

    print("✅ Folders ready:")
    print("📂 Dataset Dir :", DATASET_DIR)
    print("📂 Images Dir  :", IMAGES_DIR)
    print("📂 Output Dir  :", OUTPUT_DIR)
    print("📂 Log Dir     :", LOG_DIR)
    print("\n⚡ Place your training images inside:", IMAGES_DIR)

    return DATASET_DIR, OUTPUT_DIR, LOG_DIR