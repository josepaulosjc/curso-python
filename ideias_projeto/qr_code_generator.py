# pip install qrcode
# pip install image
from PIL import Image
import qrcode

#item que estara embutido no qrcode
# url = 'https://www.elo7.com.br/personalizeprodutospersonalizados'
url = 'https://linktr.ee/joyamancio'

qr = qrcode.QRCode(
    version=1,
    box_size=4,
    border=5
)

qr.add_data(url)
qr.make(fit=True)

#cria a imagem com o qrcode
img = qr.make_image(fill='black', back_color='white')
img.show()