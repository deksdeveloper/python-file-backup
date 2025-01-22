import zipfile
import os
import time
from datetime import datetime

def yedek_al():
    kaynak_klasor = r"C:\Users\CASPER\Desktop\vintage\gamemodes"
    hedef_klasor = r"C:\Users\CASPER\Desktop\vintage\yedekler"
    
    suan = datetime.now()
    gun = suan.day
    saat = suan.hour
    dakika = suan.minute
    
    yedek_adi = f"Gün{gun:02d}-Saat{saat:02d}-Dakika{dakika:02d}"
    hedef_yedek_dosya = os.path.join(hedef_klasor, yedek_adi + '.zip')
    
    with zipfile.ZipFile(hedef_yedek_dosya, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(kaynak_klasor):
            if '.vs' in dirs:
                dirs.remove('.vs') 
            
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    zipf.write(file_path, os.path.relpath(file_path, kaynak_klasor))
                except PermissionError:
                    print(f"Yetersiz yetki: {file_path} dosyasıa tlanıyor")
    
    print(f"Yedek alındı: {hedef_yedek_dosya}")
    
def main():
    while True:
        yedek_al()
        time.sleep(60) 

if __name__ == "__main__":
    main()
