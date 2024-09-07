import os
import subprocess
import sys

def build_wheel(package_path):
    current_dir = os.getcwd()
    os.chdir(package_path)
    try:
        subprocess.check_call([sys.executable, "setup.py", "bdist_wheel"])
    finally:
        os.chdir(current_dir)

def main():
    packages = [
        "./external/engine",
        "./external/cv",
        "./external/det"
    ]
    
    for package in packages:
        print(f"Building wheel for {package}...")
        build_wheel(package)
        print(f"Wheel built for {package}")

if __name__ == "__main__":
    main()