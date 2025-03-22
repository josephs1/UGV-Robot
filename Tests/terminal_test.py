import subprocess

# Open a new terminal window (Command Prompt)
#subprocess.Popen(['cmd', '/K', 'echo "Hello from Jetson!"'])
#subprocess.Popen(['start', 'cmd', '/K', 'echo "Jetson Nano Terminal Output"'], shell=True)
subprocess.Popen(['start', 'powershell', '-NoExit', 'echo "Jetson Nano Terminal Output"'], shell=True)