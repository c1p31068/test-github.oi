import pyautogui as pgui
import time

#スクラッチのタブをクリックする
pgui.click(300, 10)
time.sleep(2)

#拡大
big = "big.png"
location = pgui.locateOnScreen(big)
x, y = pgui.center(location)
pgui.click(x, y)
time.sleep(2)

#録画
pgui.hotkey("winleft","altleft","r")
time.sleep(1)

#旗の画像の座標を検知してクリックする
flag = "flag1.png"
location = pgui.locateOnScreen(flag)
x, y = pgui.center(location)
pgui.click(x, y)

#操作（各級の操作を入力）
time.sleep(19)

#録画停止
pgui.hotkey("winleft","altleft","r")

#ストップの部分をクリックする
stop = "stop.png"
location = pgui.locateOnScreen(stop)
x, y = pgui.center(location)
pgui.click(x, y)
time.sleep(4)

#homepageのタブをクリック
pgui.click(100, 10)
time.sleep(2)
