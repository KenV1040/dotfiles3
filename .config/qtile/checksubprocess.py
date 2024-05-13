import subprocess


venv_path = "/home/ken/.config/qtile/qtile-venv/bin/python"
script = "/home/ken/.config/qtile/qtile-script-venv.py"
subprocess.run([venv_path, script])
