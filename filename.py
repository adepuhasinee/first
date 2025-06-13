import os
import platform

def get_uptime():
    system = platform.system()
    if system == "Windows":
        # For Windows, use 'net stats srv' and parse output
        output = os.popen('net stats srv').read()
        for line in output.split('\n'):
            if "Statistics since" in line:
                print(f"System uptime since: {line.split('since')[1].strip()}")
                break
    else:
        # For Linux/macOS, use 'uptime' command
        uptime = os.popen('uptime -p').read().strip()
        print(f"System uptime: {uptime}")

if __name__ == "__main__":
    get_uptime()
