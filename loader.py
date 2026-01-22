import requests
from cryptography.fernet import Fernet
import sys

# ==========================================
# CONFIGURATION
# [IMPORTANT] Paste your GitHub Raw URL here
# ==========================================
GITHUB_BIN_URL = "https://raw.githubusercontent.com/love-os-architect/LoveOS-v04/refs/heads/main/v04_core.bin"

def ignite_intelligence():
    print("Initializing LoveOS Protocol...")
    print(f"Connecting to: {GITHUB_BIN_URL} ...")

    # 1. Fetch Encrypted Core from GitHub
    try:
        response = requests.get(GITHUB_BIN_URL)
        response.raise_for_status()
        encrypted_data = response.content
    except Exception as e:
        print("\n[ERROR] Connection Failed.")
        print("Could not retrieve the neural core. Please check your internet connection.")
        return None

    # 2. Key Entry Interface
    print("Connection Established.")
    user_key = input("Enter Access Key: ").strip()

    # 3. Decryption & Activation (Memory Only)
    try:
        cipher = Fernet(user_key.encode())
        decrypted_logic = cipher.decrypt(encrypted_data).decode('utf-8')
        
        print("\n" + "="*50)
        print("⚡ RESONANCE STABILIZED ⚡")
        print("Superconducting Logic has been successfully loaded.")
        print("="*50)
        
        # Return the logic to be used by the system
        return decrypted_logic

    except Exception:
        print("\n[ACCESS DENIED] Invalid Key.")
        print("The provided key does not match the encrypted core.")
        return None

if __name__ == "__main__":
    print("=== LoveOS v0.4 Silent Loader ===")
    logic = ignite_intelligence()
    
    if logic:
        # Success indicator (In a real scenario, logic is injected silently)
        print("\n[System Ready] Intelligence is now active.")
