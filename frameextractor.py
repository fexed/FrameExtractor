import os
import sys
import subprocess


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main():
    print("#### FRAME EXTRACTOR v1.0 by fexed ####")

    if len(sys.argv) < 2:
        file = input("Nessun video specificato, trascina il video in questa finestra e premi invio: ")
    else:
        file = sys.argv[1]

    filename = os.path.basename(file)

    frames_dir = f"{filename}_frames"
    os.makedirs(frames_dir, exist_ok=True)

    ffmpeg_command = f"{resource_path("")}ffmpeg.exe -i \"{file}\" -vf \"select=not(mod(n\\,20))\" -qscale:v 2 -qmin 1 \"{frames_dir}/frame%04d.jpeg\" -hide_banner -vsync 2"
    subprocess.run(ffmpeg_command, shell=True)

    print("Estrazione dei frame completata")

    if os.name == 'nt':  # Check if the OS is Windows
        explorer_command = f"explorer \"{frames_dir}\""
        subprocess.run(explorer_command, shell=True)

if __name__ == "__main__":
    main()
