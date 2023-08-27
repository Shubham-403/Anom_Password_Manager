import subprocess
from rich import print as printc

class installReq():
    def installPackages(self):
        packList = ["MySQL-connector-python", "rich", "cryptography", "maskpass", "pyperclip"]
        for package in packList:
            try:
                subprocess.check_call(["pip", "install", package])
                printc(f"[green]Successfully installed {package}")
            except subprocess.CalledProcessError as e:
                printc(f"Error installing {package}: {e}")

