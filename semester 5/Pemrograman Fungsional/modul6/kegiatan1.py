# Lengkapi kode dibawah untuk menjawab soal diatas ya 
# TODO 0 : Import library lain yang dibutuhkan 
from PIL import Image, ImageDraw, ImageFont
 
# TODO 1: Lakukan load image pada variabel berikut 
# hint: kalian bisa gunakan fungsi open() 
gambarku = Image.open('image/umm.jpg') 
# TODO 2: Ubah gambar menjadi hitam-putih 
# hint: kalian bisa gunakan fungsi convert() 
gambarBW = gambarku.convert("L") 
# TODO 3: Tambahkan text sesuai kriteria. 
draw = ImageDraw.Draw(gambarBW)
text = "testing" 
font = ImageFont.truetype('Arial.ttf', 24) 
_, _, text_width, text_height = draw.textbbox((0, 0), text, font=font) 
text_x = (gambarku.width - text_width) // 2 
text_y = 20 
draw.text((text_x, text_y), text, font=font, fill='black') 
# TODO 4: Simpan gambar hasil edit menggunakan fungsi save() 
gambarBW.save('percobaan_satu.jpg') 
# TODO 5: Tampilkan hasil akhir gambar 
gambarBW.show()