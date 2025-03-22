import platform
import psutil

def fetch_system_info():
    print("📊 System Info:")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"CPU: {platform.processor()}")
    print(f"RAM: {psutil.virtual_memory().total // (1024 ** 3)} GB\n")
