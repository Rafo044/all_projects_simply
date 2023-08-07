import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.drawing.image import Image

# Matplotliblə qrafik yarat
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
plt.xlabel('X Değeri')
plt.ylabel('Y Değeri')
plt.title('Örnek Grafiği')

# Grafiki png olaraq yaddasa yaz
plt.savefig('plot.png')

# Excel Workbook və worksheet aç
wb = Workbook()
ws = wb.active

# Png dosyasını worksheete əlavə et
img = Image('plot.png')
ws.add_image(img, 'A1')

# Excel dosyasını yadda saxla
wb.save('data.xlsx')
