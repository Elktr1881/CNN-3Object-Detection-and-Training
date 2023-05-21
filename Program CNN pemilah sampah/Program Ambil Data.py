import cv2

# Inisialisasi kamera
cap = cv2.VideoCapture(1)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1)

x1 = 390
y1 = 150
x2 = 590
y2 = 350

# Direktori untuk menyimpan gambar
# save_dir = r'D:\Project-project\Pemilah Sampah\Datasheet created\Botol\botol'
# save_dir = r'D:\Project-project\Pemilah Sampah\Datasheet created\train\Kertas\kertas'
save_dir = r'D:\Project-project\Pemilah Sampah\Datasheet created\Datapicture\train\Botol\kertas'
# save_dir = r'D:\Project-project\Fefi_Arm\Datasheet\train\Hitam\Htm'

# Counter untuk penomoran gambar
count = 0

while True:
    # Ambil gambar dari kamera
    ret, frame = cap.read()
    cropped_image = frame[y1:y2, x1:x2]

    # Tampilkan gambar
    cv2.rectangle(frame, (x1-2, y1-2), (x2+2, y2+2), (0, 255, 255), 2)
    cv2.imshow('Capture Image', frame)

    # Jika tombol 's' ditekan, simpan gambar
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Buat nama file dengan format 'img_[counter].jpg'
        filename = '{}.jpg'.format(count)

        # Simpan gambar ke direktori
        cv2.imwrite(save_dir + filename, cropped_image)
        print('Gambar {} disimpan'.format(filename))

        # Tambahkan counter
        count += 1

    # Jika tombol 'q' ditekan, keluar dari loop
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup kamera dan jendela tampilan gambar
cap.release()
cv2.destroyAllWindows()