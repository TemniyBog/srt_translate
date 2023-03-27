from pathlib import Path
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import shutil
from os import path

def save(file):
    driver = webdriver.Chrome()
    driver.get('https://translate-subtitles.com/ru')
    PassportCopy = driver.find_element(By.ID, 'file')
    PassportCopy.send_keys(file)
    time.sleep(10)  # скачивание русского файла

def main():
    directory = 'путь_до_папки_с_субтитрами' #ВПИСАТЬ НУЖНУЮ ДИРЕКТОРИЮ
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.srt'):
                our_file = os.path.join(root, file) #файл англ субтитры
                destination_path = os.path.join(root) #путь до этого файла
                save(our_file)

                path_load = 'путь_до_загрузочной_папки' #ВПИСАТЬ ПАПКУ, КУДА ПАДAЮТ СУБТИТРЫ НА РУССКОМ
                pathlist = Path(path_load).glob('*.srt')  # нашли русский файл
                for path1 in pathlist:
                    if path.exists(path1):
                        new_location = shutil.copy(path1, destination_path)
                        print("% s перемещен в указанное место % s" % (path1, new_location))
                        os.remove(path1)
                        os.remove(our_file) #удаляем англ файл
                    else:
                        print("Файл не существует.")

if __name__ == '__main__':
    main()