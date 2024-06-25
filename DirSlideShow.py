import os
import sys
import tkinter as tk
from PIL import Image, ImageTk
import random

pictures = []
picindex = []

def scan_pictures(dirname, pictures):
  for item in os.listdir(dirname):
    item_path = os.path.join(dirname, item)
    # ファイルであるかのチェック
    if os.path.isfile(item_path):
        # 画像ファイルの拡張子をチェック
        if item_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
            pictures.append(item_path.replace('\\', '\\\\'))
        
    # ディレクトリである場合の再帰呼び出し
    elif os.path.isdir(item_path):
      scan_pictures(item_path, pictures)

def make_random_indexes(pictures):
  indexes = list(range(len(pictures)))
  random.shuffle(indexes)
  return indexes


def popup_menu(event):
    context_menu.post(event.x_root, event.y_root)

#
# 画像表示
#
def show_image():
  global root, photo, picindex, pictures
  # 次の画像
  if len(picindex) == 0:
    picindex = make_random_indexes(pictures)
  i = picindex.pop(0)

  #
  window_width = root.winfo_width()
  window_height = root.winfo_height()
  # 画像を読み込む
  image = Image.open(pictures[i])
  img_width, img_height = image.size
  img_ratio = min(window_width/img_width, window_height/img_height)
  new_width = int(img_width * img_ratio)
  new_height = int(img_height * img_ratio)
  resized_image = image.resize((new_width, new_height), Image.LANCZOS)
  # PIL ImageをTkinter PhotoImageに変換
  photo = ImageTk.PhotoImage(resized_image)
  label.config(image=photo)
  root.after(10000, show_image) # 次の画像を表示するまで待機（ms）


#
# scan
#
path = sys.argv[1] if len(sys.argv) > 1 else '.'
scan_pictures(path, pictures)

#
# tkinter main loop
#
root = tk.Tk()
root.title("DirSlideShow")
root.attributes('-fullscreen', True)
root.configure(bg = '#606060')
#root.geometry("800x600")

label = tk.Label(root, text="initialized")
label.pack()

# コンテキストメニューの作成
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="終了", command=root.quit)
# コンテキストメニューをウィンドウにバインド
label.bind("<Button-3>", popup_menu)
root.bind('<Escape>', lambda e: root.quit())

# show_image()
root.after(100, show_image)

root.mainloop()

