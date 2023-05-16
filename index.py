from PIL import Image, ImageFont, ImageDraw

barWidth = 300
barHeight = 30

# 建立色彩模式為 RGBA，尺寸 Width x Height 的空白(255, 255, 255)圖片
img = Image.new('RGBA', (barWidth, barHeight), (255, 255, 255)) 

# 設定字型與尺寸
font = ImageFont.truetype('標楷體.ttc', 30)

# 準備在圖片上繪圖
draw = ImageDraw.Draw(img)  

# 將文字置中畫入圖片
draw.text(xy=(barWidth/2, barHeight/2), anchor='mm', text='Hello World!', fill='black', font=font, stroke_width=2, stroke_fill='white')

# Show Image
img.show()