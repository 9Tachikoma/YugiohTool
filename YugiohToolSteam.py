# !/usr/bin/python
# coding:utf-8

"""
@author: zyatom
@contact: 70906346@qq.com
@software: PyCharm
@file: YugiohToolMoniqi.py
@time: 2019/4/25 20:02
"""
import importlib
import random
import sys
import win32api
import win32gui
import time
import pyautogui as pyg
import configparser
import logging
import base64

from CaiDan_steam_png import img as caidan
from Chongshi_steam_png import img as chongshi
from duorenwu_steam_png import img as duorenwu
from Hao_steam_png import img as hao
from Jieshu_steam_png import img as jiesu
from JueDou_steam_png import img as juedou
from QueRen_steam_png import img as queren
from XiaYiBu_steam_png import img as xiayibu
from zhongduan_steam_png import img as zhongduan
from zhujiemian_steam_png import img as zhujiemian
from fanhui_steam_png import img as fanhui
from lvse_steam_png import img as lvse
from zhandou_steam_png import img as zhandou
from shijuedou_steam_png import img as shijuedou
from kc_steam_png import img as kcb
from paiming_steam_png import img as paimin
from xiuxian_steam_png import img as xiuxian
from kunnan_png import img as kunnan
from zidongjuedou_png import img as zidongjuedou
from zudui_png import img as zudui
from feichangkunnan_png import img as fckunnan
from clear_png import img as clear
from guanbi_steam_png import img as guanbi
from zandouQueRen_steam_png import img as zhandouqueren

importlib.reload(sys)

tuisong_time = None


class Networkerror(RuntimeError):
	def __init__(self, arg):
		self.args = arg


class Steam:
	def __init__(self, wdname, free):  # 初始化
		self.logger = logging.getLogger()  # 不加名称设置root logger
		self.logger.setLevel(logging.DEBUG)
		formatter = logging.Formatter(
			'%(asctime)s - %(name)s - %(levelname)s: - %(message)s',
			datefmt='%Y-%m-%d %H:%M:%S')
		fh = logging.FileHandler('log.txt')  # 使用FileHandler输出到文件
		fh.setLevel(logging.DEBUG)
		fh.setFormatter(formatter)
		ch = logging.StreamHandler()  # 使用StreamHandler输出到屏幕
		ch.setLevel(logging.DEBUG)
		ch.setFormatter(formatter)
		self.logger.addHandler(ch)  # 添加两个Handler
		self.logger.addHandler(fh)
		logging.getLogger("urllib3.connectionpool").setLevel(logging.WARNING)  # 设置requests不输出日志

		win32api.keybd_event(13, 0, 0, 0)  #
		self.hwnd = win32gui.FindWindow(0, wdname)  # 取得窗口句柄
		if not self.hwnd:
			print("窗口找不到，请打开【%s】" % wdname)
			exit()
		win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
		size = win32gui.GetWindowRect(self.hwnd)
		# print(size)
		global topx, topy, topx1, topy1
		topx, topy, topx1, topy1 = size[0], size[1], size[2], size[3]
		tmp = open('YugiohTool/api-cd.dll', 'wb')  # 创建临时的文件
		tmp.write(base64.b64decode(caidan))  # 把这个图片解码出来，写入文件中去。
		tmp = open('YugiohTool/api-cs.dll', 'wb')
		tmp.write(base64.b64decode(chongshi))
		tmp = open('YugiohTool/api-drw.dll', 'wb')
		tmp.write(base64.b64decode(duorenwu))
		tmp = open('YugiohTool/api-h.dll', 'wb')
		tmp.write(base64.b64decode(hao))
		tmp = open('YugiohTool/api-js.dll', 'wb')
		tmp.write(base64.b64decode(jiesu))
		tmp = open('YugiohTool/api-jd.dll', 'wb')
		tmp.write(base64.b64decode(juedou))
		tmp = open('YugiohTool/api-qr.dll', 'wb')
		tmp.write(base64.b64decode(queren))
		tmp = open('YugiohTool/api-xyb.dll', 'wb')
		tmp.write(base64.b64decode(xiayibu))
		tmp = open('YugiohTool/api-zd.dll', 'wb')
		tmp.write(base64.b64decode(zhongduan))
		tmp = open('YugiohTool/api-zjm.dll', 'wb')
		tmp.write(base64.b64decode(zhujiemian))
		tmp = open('YugiohTool/api-fh.dll', 'wb')
		tmp.write(base64.b64decode(fanhui))
		tmp = open('YugiohTool/api-ls.dll', 'wb')
		tmp.write(base64.b64decode(lvse))
		tmp = open('YugiohTool/api-zdu.dll', 'wb')
		tmp.write(base64.b64decode(zhandou))
		tmp = open('YugiohTool/api-sjd.dll', 'wb')
		tmp.write(base64.b64decode(shijuedou))
		tmp = open('YugiohTool/api-kc.dll', 'wb')
		tmp.write(base64.b64decode(kcb))
		tmp = open('YugiohTool/api-pm.dll', 'wb')
		tmp.write(base64.b64decode(paimin))
		tmp = open('YugiohTool/api-xx.dll', 'wb')
		tmp.write(base64.b64decode(xiuxian))
		tmp = open('YugiohTool/api-kn.dll', 'wb')
		tmp.write(base64.b64decode(kunnan))
		tmp = open('YugiohTool/api-zdjd.dll', 'wb')
		tmp.write(base64.b64decode(zidongjuedou))
		tmp = open('YugiohTool/api-zdui.dll', 'wb')
		tmp.write(base64.b64decode(zudui))
		tmp = open('YugiohTool/api-fckn.dll', 'wb')
		tmp.write(base64.b64decode(fckunnan))
		tmp = open('YugiohTool/api-cl.dll', 'wb')
		tmp.write(base64.b64decode(clear))
		tmp = open('YugiohTool/api-gb.dll', 'wb')
		tmp.write(base64.b64decode(guanbi))
		tmp = open('YugiohTool/api-zdqr.dll', 'wb')
		tmp.write(base64.b64decode(zhandouqueren))
		tmp.close()
		if free == "1":
			print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ 脚本交流和售后群９０８５６３５０３　　　　　　　　　　　　　")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ 使用前请务必先阅读＂脚本使用方法．ｄｏｃｘ＂　　　　　　　")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ 当前版本为完整版，有任何问题或者建议请联系我　　　　　　　")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ ★★★★★要关闭脚本请把鼠标放到屏幕左上角停留２秒钟★★★★★ 　　 ")
			print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
		if free == "2":
			print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ 试用版脚本交流群８１９８２７８４２　　　　　　　　　　　　")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ 使用前请务必先阅读＂脚本使用方法．ｄｏｃｘ＂　　　　　　　")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ 当前版本为试用版，挂机三十分钟后停止，继续试用请重新打开脚本")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ ★★★★★要关闭脚本请把鼠标放到屏幕左上角停留２秒钟★★★★★ 　　 　")
			print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

	@staticmethod
	def dianji(x, y):
		pyg.moveTo(x + random.randint(-6, 6), y + random.randint(-6, 6))
		time.sleep(0.1)
		pyg.mouseDown()
		pyg.mouseUp()

	@staticmethod
	def dianji_guding(x, y):
		x1 = topx + int((topx1 - topx) * x) + random.randint(-6, 6)
		y1 = topy + int((topy1 - topy) * y) + random.randint(-6, 6)
		pyg.moveTo(x1, y1)
		time.sleep(0.1)
		pyg.mouseDown()
		pyg.mouseUp()

	@staticmethod
	def tuodong(x, y):
		pyg.moveTo(x, y + 30)
		time.sleep(0.2)
		pyg.dragRel(0, -200, 0.2)

	@staticmethod
	def tuodong_guding(x, y):
		x1 = topx + int((topx1 - topx) * x)
		y1 = topy + int((topy1 - topy) * y)
		pyg.moveTo(x1, y1 + 30)
		time.sleep(0.2)
		pyg.dragRel(0, -200, 0.2)

	def pvp_tolose_steam(self, arg):  # pvp自杀
		win32api.keybd_event(13, 0, 0, 0)  #
		win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
		mode = None
		cf = configparser.ConfigParser()
		cf.read("config.ini")  # 读取配置文件
		count = int(cf.get("config", "count"))
		while True:
			time.sleep(0.5)
			self.dianji_guding(0.4663, 0.0857)  # 点击空白
			zjm = pyg.locateOnScreen('YugiohTool/api-zjm.dll', confidence=0.80, grayscale=True)
			haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
			xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
			cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
			fhui = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
			if zjm is not None:
				self.dianji_guding(0.4537, 0.9679)  # 点击pvp门固定点
				time.sleep(1)

				# 检测模式 截图模式
				# if zjm is not None: # 该检测模式
				# 	self.dianji_guding(0.4537, 0.9679)  # 点击pvp门固定点
				# 	time.sleep(1)
				kc = pyg.locateOnScreen('YugiohTool/api-kc.dll', confidence=0.80, grayscale=True)
				pm = pyg.locateOnScreen('YugiohTool/api-pm.dll', confidence=0.80, grayscale=True)
				if str(arg) == '1':
					mode = kc
				elif str(arg) == '2':
					mode = pm
				elif str(arg) == '3':
					self.tuodong_guding(0.3, 0.8109)
					time.sleep(1)
					mode = pyg.locateOnScreen('YugiohTool/api-xx.dll', confidence=0.80, grayscale=True)
				if mode is not None:
					s_x, s_y = pyg.center(mode)
					self.dianji(s_x, s_y)  # 点击决斗模式
					time.sleep(2)
					while True:
						time.sleep(0.5)
						self.dianji_guding(0.4663, 0.0857)
						jd = pyg.locateOnScreen('YugiohTool/api-jd.dll', confidence=0.80, grayscale=False)
						haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
						cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80, grayscale=True)
						xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
						qr = pyg.locateOnScreen('YugiohTool/api-qr.dll', confidence=0.80, grayscale=True)
						cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
						if cs is not None:
							s_x, s_y = pyg.center(cs)
							self.dianji(s_x, s_y)  # 点击重试
						if jd is not None:
							s_x, s_y = pyg.center(jd)
							self.dianji(s_x, s_y)  # 点击决斗
							count = count + 1
							cf.set('config', 'count', str(count))
							cf.write(open("config.ini", 'w'))  # 写入count次数
							self.logger.info('决斗！已对战%s次', str(count))
						if cd is not None:
							s_x, s_y = pyg.center(cd)
							self.dianji(s_x, s_y)  # 点击菜单
							time.sleep(0.5)
							js = pyg.locateOnScreen('YugiohTool/api-js.dll', confidence=0.80, grayscale=True)
							if js is not None:
								s_x, s_y = pyg.center(js)
								self.dianji(s_x, s_y)  # 点击结束回合
						if qr is not None:
							s_x, s_y = pyg.center(qr)
							self.dianji_guding(0.4561, 0.6776)
							time.sleep(0.2)
							self.dianji_guding(0.5696, 0.6776)
							time.sleep(0.2)
							self.dianji(s_x, s_y)  # 点击确认
						if haod is not None:
							s_x, s_y = pyg.center(haod)
							self.dianji(s_x, s_y)  # 点击好
						if xyb is not None:
							s_x, s_y = pyg.center(xyb)
							self.dianji(s_x, s_y)  # 点击下一步
			if haod is not None:
				s_x, s_y = pyg.center(haod)
				self.dianji(s_x, s_y)  # 点击好
				time.sleep(1)
			if xyb is not None:
				s_x, s_y = pyg.center(xyb)
				self.dianji(s_x, s_y)  # 点击下一步
				time.sleep(1)
			if cs is not None:
				s_x, s_y = pyg.center(cs)
				self.dianji(s_x, s_y)  # 点击重试
			if fhui is not None:
				s_x, s_y = pyg.center(fhui)
				self.dianji(s_x, s_y)  # 点击返回
				time.sleep(1)
				fhui2 = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
				if fhui2 is not None:
					s_x, s_y = pyg.center(fhui2)
					self.dianji(s_x, s_y)  # 点击返回
					time.sleep(1)

	def chuansongmen_steam(self):  # 十级门
		win32api.keybd_event(13, 0, 0, 0)  #
		win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
		cf = configparser.ConfigParser()
		cf.read("config.ini")  # 读取配置文件
		csmcount = int(cf.get("config", "csmcount"))
		while True:
			time.sleep(0.5)
			self.dianji_guding(0.4663, 0.0857)  # 点击空白
			zjm = pyg.locateOnScreen('YugiohTool/api-zjm.dll', confidence=0.80, grayscale=True)
			haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
			xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
			cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
			fhui = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
			if zjm is not None:
				self.dianji_guding(0.3460, 0.9708)  # 点击传送门固定点
				time.sleep(5)
				sjd = pyg.locateOnScreen('YugiohTool/api-sjd.dll', confidence=0.80, grayscale=False)
				haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
				xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
				time.sleep(0.3)
				if sjd is not None:
					self.dianji_guding(0.3913, 0.6931)  # 点击等级:10
					possjd = sjd
					s_x, s_y = pyg.center(possjd)
					self.dianji(s_x, s_y)  # 点击决斗
					huihecount = 1
					for i in range(25):
						time.sleep(0.5)
						self.dianji_guding(0.5723, 0.0926)
						sjd = pyg.locateOnScreen('YugiohTool/api-sjd.dll', confidence=0.80, grayscale=False)
						if sjd is not None:
							s_x, s_y = pyg.center(sjd)
							self.dianji(s_x, s_y)  # 点击决斗
							csmcount = csmcount + 1
							cf.set('config', 'csmcount', str(csmcount))
							cf.write(open("config.ini", 'w'))  # 写入count次数
							self.logger.info('第%s次传送门>>>>>>', str(csmcount))
							huihecount = 1
							break
					try:
						for i in range(100):
							gongjicount = 0
							time.sleep(0.5)
							self.dianji_guding(0.4663, 0.0857)
							cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80, grayscale=True)
							haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
							if cd is not None:
								self.dianji_guding(0.4783, 0.9328)  # 点击卡牌
								time.sleep(0.5)
								self.dianji_guding(0.4603, 0.7448)  # 点击通常召唤
								time.sleep(2)
								s_x, s_y = pyg.center(cd)
								self.dianji(s_x, s_y)  # 点击菜单
								time.sleep(1)
								zdu = pyg.locateOnScreen('YugiohTool/api-zdu.dll', confidence=0.80, grayscale=True)
								if zdu is not None:
									zdu_x, zdu_y = pyg.center(zdu)
									self.dianji(zdu_x, zdu_y)  # 点击战斗
									time.sleep(0.5)
									for x in range(10):
										time.sleep(0.3)
										ls = pyg.locateOnScreen('YugiohTool/api-ls.dll', confidence=0.80,
										                        grayscale=False)
										haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80,
										                          grayscale=True)
										if ls is not None:
											ls_x, ls_y = pyg.center(ls)
											self.tuodong(ls_x, ls_y)  # 拖动攻击
											gongjicount = gongjicount + 1
											time.sleep(1)
										if haod is not None:
											haod_x, haod_y = pyg.center(haod)
											self.dianji(haod_x, haod_y)  # 点击好
											raise Networkerror("Bad hostname")
										if gongjicount >= huihecount or gongjicount >= 3:  # 结束攻击
											time.sleep(1)
											for j in range(25):
												time.sleep(0.3)
												# 检测菜单
												cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80,
												                        grayscale=True)
												if cd is not None:
													s_x, s_y = pyg.center(cd)
													self.dianji(s_x, s_y)  # 点击菜单
													time.sleep(0.5)
													js = pyg.locateOnScreen('YugiohTool/api-js.dll', confidence=0.80,
													                        grayscale=True)
													if js is not None:
														s_x, s_y = pyg.center(js)
														self.dianji(s_x, s_y)  # 点击结束回合
														huihecount = huihecount + 1
														time.sleep(1)
														break
											break
								else:
									self.dianji_guding(0.6302, 0.6797)  # 点击结束回合
									huihecount = huihecount + 1
							if haod is not None:
								haod_x, haod_y = pyg.center(haod)
								self.dianji(haod_x, haod_y)  # 点击好
								raise Networkerror("Bad hostname")
					except Networkerror:
						pass

			if haod is not None:
				s_x, s_y = pyg.center(haod)
				self.dianji(s_x, s_y)  # 点击好
			if xyb is not None:
				s_x, s_y = pyg.center(xyb)
				self.dianji(s_x, s_y)  # 点击下一步
			if cs is not None:
				s_x, s_y = pyg.center(cs)
				self.dianji(s_x, s_y)  # 点击重试
			if fhui is not None:
				s_x, s_y = pyg.center(fhui)
				self.dianji(s_x, s_y)
				time.sleep(1)
				fhui2 = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
				if fhui2 is not None:
					s_x, s_y = pyg.center(fhui2)
					self.dianji(s_x, s_y)  # 点击返回
					time.sleep(1)

	def pvp_xiuxian_towin_steam(self):  # pvp休闲towin
		win32api.keybd_event(13, 0, 0, 0)  #
		win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
		cf = configparser.ConfigParser()
		cf.read("config.ini")  # 读取配置文件
		count = int(cf.get("config", "count"))
		while True:
			time.sleep(0.5)
			self.dianji_guding(0.4663, 0.0857)  # 点击空白
			zjm = pyg.locateOnScreen('YugiohTool/api-zjm.dll', confidence=0.80, grayscale=True)
			haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
			xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
			cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
			fhui = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
			if zjm is not None:
				self.dianji_guding(0.4537, 0.9679)  # 点击pvp门固定点
				time.sleep(2)
				self.tuodong_guding(0.3949, 0.814)
				time.sleep(2)
				xx = pyg.locateOnScreen('YugiohTool/api-xx.dll', confidence=0.80, grayscale=True)
				time.sleep(1)
				if xx is not None:
					s_x, s_y = pyg.center(xx)
					self.dianji(s_x, s_y)  # 点击休闲
					time.sleep(2)
					while True:
						time.sleep(0.5)
						self.dianji_guding(0.4663, 0.0857)  # 点击空白
						jd = pyg.locateOnScreen('YugiohTool/api-jd.dll', confidence=0.80, grayscale=False)
						haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
						xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
						qr = pyg.locateOnScreen('YugiohTool/api-qr.dll', confidence=0.80, grayscale=True)
						cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
						huihecount = 1
						if cs is not None:
							s_x, s_y = pyg.center(cs)
							self.dianji(s_x, s_y)  # 点击重试
						if jd is not None:
							s_x, s_y = pyg.center(jd)
							self.dianji(s_x, s_y)  # 点击决斗
							count = count + 1
							cf.set('config', 'count', str(count))
							cf.write(open("config.ini", 'w'))  # 写入count次数
							self.logger.info('决斗！已对战%s次', str(count))
							for i in range(25):
								time.sleep(0.3)
								self.dianji(s_x, s_y)
								zd = pyg.locateOnScreen('YugiohTool/api-zd.dll', confidence=0.80, grayscale=True)
								if zd is not None:
									break
								cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
								if cs is not None:
									s_x, s_y = pyg.center(cs)
									self.dianji(s_x, s_y)  # 点击重试
							try:
								a = 0
								while a < 150:
									gongjicount = 0
									time.sleep(0.5)
									self.dianji_guding(0.4663, 0.0857)
									cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80, grayscale=True)
									haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
									a = a + 1
									if cd is not None:
										a = 1
										self.dianji_guding(0.4783, 0.9328)  # 点击卡牌
										time.sleep(0.5)
										self.dianji_guding(0.4603, 0.7448)  # 点击通常召唤
										time.sleep(2)
										for k in range(100):  # 等菜单
											time.sleep(0.5)
											cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80,
											                        grayscale=True)
											if cd is not None:
												s_x, s_y = pyg.center(cd)
												self.dianji(s_x, s_y)  # 点击菜单
												break
										time.sleep(1)
										zdu = pyg.locateOnScreen('YugiohTool/api-zdu.dll', confidence=0.80,
										                         grayscale=True)
										if zdu is not None:
											zdu_x, zdu_y = pyg.center(zdu)
											self.dianji(zdu_x, zdu_y)  # 点击战斗
											time.sleep(0.5)
											try:
												for h in range(100):  # 等菜单
													time.sleep(0.5)
													cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80,
													                        grayscale=True)

													if cd is not None:
														for g in range(50):  # 攻击
															time.sleep(0.5)
															lvs = pyg.locateOnScreen('YugiohTool/api-ls.dll',
															                         confidence=0.80,
															                         grayscale=False)
															haod = pyg.locateOnScreen('YugiohTool/api-h.dll',
															                          confidence=0.80,
															                          grayscale=True)
															zdqr = pyg.locateOnScreen('YugiohTool/api-zdqr.dll',
															                          confidence=0.80,
															                          grayscale=True)
															if lvs is not None:
																ls_x, ls_y = pyg.center(lvs)
																self.tuodong(ls_x, ls_y)  # 拖动攻击
																gongjicount = gongjicount + 1
																time.sleep(1)
															if zdqr is not None:
																ls_x, ls_y = pyg.center(zdqr)
																self.tuodong(ls_x, ls_y)  # 点击确认
																time.sleep(1)
															if haod is not None:
																haod_x, haod_y = pyg.center(haod)
																self.dianji(haod_x, haod_y)  # 点击好
																raise Networkerror("Bad hostname")
															if gongjicount >= huihecount or gongjicount >= 3:  # 结束攻击
																time.sleep(0.5)
																for j in range(25):
																	time.sleep(0.3)
																	# 检测菜单
																	cd = pyg.locateOnScreen('YugiohTool/api-cd.dll',
																	                        confidence=0.80,
																	                        grayscale=True)
																	if cd is not None:
																		s_x, s_y = pyg.center(cd)
																		self.dianji(s_x, s_y)  # 点击菜单
																		time.sleep(0.5)
																		js = pyg.locateOnScreen('YugiohTool/api-js.dll',
																		                        confidence=0.80,
																		                        grayscale=True)
																		if js is not None:
																			s_x, s_y = pyg.center(js)
																			self.dianji(s_x, s_y)  # 点击结束回合
																			huihecount = huihecount + 1
																			time.sleep(1)
																			raise StopIteration("Bad hostname")
																break
															if g == 9:
																for f in range(25):  # 检测菜单
																	time.sleep(0.3)
																	cd = pyg.locateOnScreen('YugiohTool/api-cd.dll',
																	                        confidence=0.80,
																	                        grayscale=True)
																	if cd is not None:
																		s_x, s_y = pyg.center(cd)
																		self.dianji(s_x, s_y)  # 点击菜单
																		time.sleep(0.5)
																		js = pyg.locateOnScreen('YugiohTool/api-js.dll',
																		                        confidence=0.80,
																		                        grayscale=True)
																		if js is not None:
																			s_x, s_y = pyg.center(js)
																			self.dianji(s_x, s_y)  # 点击结束回合
																			huihecount = huihecount + 1
																			time.sleep(1)
																			raise StopIteration("Bad hostname")
											except StopIteration:
												pass
										else:
											self.dianji_guding(0.6302, 0.6797)  # 点击结束回合
											huihecount = huihecount + 1
									if haod is not None:
										haod_x, haod_y = pyg.center(haod)
										self.dianji(haod_x, haod_y)  # 点击好
										raise Networkerror("Bad hostname")
							except Networkerror:
								pass
						if qr is not None:
							s_x, s_y = pyg.center(qr)
							self.dianji_guding(0.4561, 0.6776)
							time.sleep(0.2)
							self.dianji_guding(0.5696, 0.6776)
							time.sleep(0.2)
							self.dianji(s_x, s_y)  # 点击确认
						if haod is not None:
							s_x, s_y = pyg.center(haod)
							self.dianji(s_x, s_y)  # 点击好
						if xyb is not None:
							s_x, s_y = pyg.center(xyb)
							self.dianji(s_x, s_y)  # 点击下一步
			if haod is not None:
				s_x, s_y = pyg.center(haod)
				self.dianji(s_x, s_y)  # 点击好
			if xyb is not None:
				s_x, s_y = pyg.center(xyb)
				self.dianji(s_x, s_y)  # 点击下一步
			if cs is not None:
				s_x, s_y = pyg.center(cs)
				self.dianji(s_x, s_y)  # 点击重试
			if fhui is not None:
				s_x, s_y = pyg.center(fhui)
				self.dianji(s_x, s_y)  # 点击返回
				time.sleep(1)
				fhui2 = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
				if fhui2 is not None:
					s_x, s_y = pyg.center(fhui2)
					self.dianji(s_x, s_y)  # 点击返回
					time.sleep(1)

	def pvp_paimin_towin_steam(self):  # pvp排名towin
		win32api.keybd_event(13, 0, 0, 0)  #
		win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
		global tuisong_time
		cf = configparser.ConfigParser()
		cf.read("config.ini")  # 读取配置文件
		count = int(cf.get("config", "count"))
		while True:
			time.sleep(0.5)
			self.dianji_guding(0.4663, 0.0857)  # 点击空白
			zjm = pyg.locateOnScreen('YugiohTool/api-zjm.dll', confidence=0.80, grayscale=True)
			haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
			xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
			cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
			fhui = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
			if zjm is not None:
				self.dianji_guding(0.4537, 0.9679)  # 点击pvp门固定点
				time.sleep(2)
				pm = pyg.locateOnScreen('YugiohTool/api-pm.dll', confidence=0.80, grayscale=True)
				time.sleep(1)
				if pm is not None:
					s_x, s_y = pyg.center(pm)
					self.dianji(s_x, s_y)  # 点击排名
					time.sleep(2)
					while True:
						time.sleep(0.5)
						self.dianji_guding(0.4663, 0.0857)  # 点击空白
						jd = pyg.locateOnScreen('YugiohTool/api-jd.dll', confidence=0.80, grayscale=False)
						haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
						xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
						qr = pyg.locateOnScreen('YugiohTool/api-qr.dll', confidence=0.80, grayscale=True)
						cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
						huihecount = 1
						if cs is not None:
							s_x, s_y = pyg.center(cs)
							self.dianji(s_x, s_y)  # 点击重试
						if jd is not None:
							s_x, s_y = pyg.center(jd)
							self.dianji(s_x, s_y)  # 点击决斗
							count = count + 1
							cf.set('config', 'count', str(count))
							cf.write(open("config.ini", 'w'))  # 写入count次数
							self.logger.info('决斗！已对战%s次', str(count))
							for i in range(25):
								time.sleep(0.3)
								self.dianji(s_x, s_y)
								zd = pyg.locateOnScreen('YugiohTool/api-zd.dll', confidence=0.80, grayscale=True)
								if zd is not None:
									break
								cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
								if cs is not None:
									s_x, s_y = pyg.center(cs)
									self.dianji(s_x, s_y)  # 点击重试
							try:
								a = 0
								while a < 150:
									gongjicount = 0
									time.sleep(0.5)
									self.dianji_guding(0.4663, 0.0857)
									cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80, grayscale=True)
									haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
									a = a + 1
									if cd is not None:
										a = 1
										self.dianji_guding(0.4783, 0.9328)  # 点击卡牌
										time.sleep(0.5)
										self.dianji_guding(0.4603, 0.7448)  # 点击通常召唤
										time.sleep(2)
										for k in range(100):  # 等菜单
											time.sleep(0.5)
											cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80,
											                        grayscale=True)
											if cd is not None:
												s_x, s_y = pyg.center(cd)
												self.dianji(s_x, s_y)  # 点击菜单
												break
										time.sleep(1)
										zdu = pyg.locateOnScreen('YugiohTool/api-zdu.dll', confidence=0.80,
										                         grayscale=True)
										if zdu is not None:
											zdu_x, zdu_y = pyg.center(zdu)
											self.dianji(zdu_x, zdu_y)  # 点击战斗
											time.sleep(0.5)
											try:
												for h in range(100):  # 等菜单
													time.sleep(0.5)
													cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80,
													                        grayscale=True)

													if cd is not None:
														for g in range(50):  # 攻击
															time.sleep(0.5)
															lvs = pyg.locateOnScreen('YugiohTool/api-ls.dll',
															                         confidence=0.80,
															                         grayscale=False)
															haod = pyg.locateOnScreen('YugiohTool/api-h.dll',
															                          confidence=0.80,
															                          grayscale=True)
															zdqr = pyg.locateOnScreen('YugiohTool/api-zdqr.dll',
															                          confidence=0.80,
															                          grayscale=True)
															if lvs is not None:
																ls_x, ls_y = pyg.center(lvs)
																self.tuodong(ls_x, ls_y)  # 拖动攻击
																gongjicount = gongjicount + 1
																time.sleep(1)
															if zdqr is not None:
																ls_x, ls_y = pyg.center(zdqr)
																self.tuodong(ls_x, ls_y)  # 点击确认
																time.sleep(1)
															if haod is not None:
																haod_x, haod_y = pyg.center(haod)
																self.dianji(haod_x, haod_y)  # 点击好
																raise Networkerror("Bad hostname")
															if gongjicount >= huihecount or gongjicount >= 3:  # 结束攻击
																time.sleep(0.5)
																for j in range(25):
																	time.sleep(0.3)
																	# 检测菜单
																	cd = pyg.locateOnScreen('YugiohTool/api-cd.dll',
																	                        confidence=0.80,
																	                        grayscale=True)
																	if cd is not None:
																		s_x, s_y = pyg.center(cd)
																		self.dianji(s_x, s_y)  # 点击菜单
																		time.sleep(0.5)
																		js = pyg.locateOnScreen('YugiohTool/api-js.dll',
																		                        confidence=0.80,
																		                        grayscale=True)
																		if js is not None:
																			s_x, s_y = pyg.center(js)
																			self.dianji(s_x, s_y)  # 点击结束回合
																			huihecount = huihecount + 1
																			time.sleep(1)
																			raise StopIteration("Bad hostname")
																break
															if g == 9:
																for f in range(25):  # 检测菜单
																	time.sleep(0.3)
																	cd = pyg.locateOnScreen('YugiohTool/api-cd.dll',
																	                        confidence=0.80,
																	                        grayscale=True)
																	if cd is not None:
																		s_x, s_y = pyg.center(cd)
																		self.dianji(s_x, s_y)  # 点击菜单
																		time.sleep(0.5)
																		js = pyg.locateOnScreen('YugiohTool/api-js.dll',
																		                        confidence=0.80,
																		                        grayscale=True)
																		if js is not None:
																			s_x, s_y = pyg.center(js)
																			self.dianji(s_x, s_y)  # 点击结束回合
																			huihecount = huihecount + 1
																			time.sleep(1)
																			raise StopIteration("Bad hostname")
											except StopIteration:
												pass
										else:
											self.dianji_guding(0.6302, 0.6797)  # 点击结束回合
											huihecount = huihecount + 1
									if haod is not None:
										haod_x, haod_y = pyg.center(haod)
										self.dianji(haod_x, haod_y)  # 点击好
										raise Networkerror("Bad hostname")
							except Networkerror:
								pass
						if qr is not None:
							s_x, s_y = pyg.center(qr)
							self.dianji_guding(0.4561, 0.6776)
							time.sleep(0.2)
							self.dianji_guding(0.5696, 0.6776)
							time.sleep(0.2)
							self.dianji(s_x, s_y)  # 点击确认
						if haod is not None:
							s_x, s_y = pyg.center(haod)
							self.dianji(s_x, s_y)  # 点击好
						if xyb is not None:
							s_x, s_y = pyg.center(xyb)
							self.dianji(s_x, s_y)  # 点击下一步
			if haod is not None:
				s_x, s_y = pyg.center(haod)
				self.dianji(s_x, s_y)  # 点击好
			if xyb is not None:
				s_x, s_y = pyg.center(xyb)
				self.dianji(s_x, s_y)  # 点击下一步
			if cs is not None:
				s_x, s_y = pyg.center(cs)
				self.dianji(s_x, s_y)  # 点击重试
			if fhui is not None:
				s_x, s_y = pyg.center(fhui)
				self.dianji(s_x, s_y)  # 点击返回
				time.sleep(1)
				fhui2 = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
				if fhui2 is not None:
					s_x, s_y = pyg.center(fhui2)
					self.dianji(s_x, s_y)  # 点击返回
					time.sleep(1)

	def huodong_zuidui_steam(self):
		win32api.keybd_event(13, 0, 0, 0)  #
		win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
		while True:
			time.sleep(0.5)
			self.dianji_guding(0.4663, 0.0857)  # 点击空白
			zjm = pyg.locateOnScreen('YugiohTool/api-zjm.dll', confidence=0.80, grayscale=True)
			haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
			cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
			fhui = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
			if zjm is not None:
				self.dianji_guding(0.5072, 0.8935)  # 点击活动固定点
				time.sleep(2)
				zdui = pyg.locateOnScreen('YugiohTool/api-zdui.dll', confidence=0.80, grayscale=True)
				time.sleep(0.3)
				if zdui is not None:
					s_x, s_y = pyg.center(zdui)
					self.dianji(s_x, s_y)  # 点击组队决斗
					while True:
						time.sleep(0.3)
						self.dianji_guding(0.4663, 0.0857)  # 点击空白
						zdjd = pyg.locateOnScreen('YugiohTool/api-zdjd.dll', confidence=0.80, grayscale=True)
						kn = pyg.locateOnScreen('YugiohTool/api-kn.dll', confidence=0.80, grayscale=True)
						zdui = pyg.locateOnScreen('YugiohTool/api-zdui.dll', confidence=0.80, grayscale=True)
						haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
						fckn = pyg.locateOnScreen('YugiohTool/api-fckn.dll', confidence=0.80, grayscale=True)
						cl = pyg.locateOnScreen('YugiohTool/api-cl.dll', confidence=0.40, grayscale=True)
						gb = pyg.locateOnScreen('YugiohTool/api-gb.dll', confidence=0.80, grayscale=True)
						if zdjd is not None:
							s_x, s_y = pyg.center(zdjd)
							self.dianji(s_x, s_y)  # 点击自动决斗
						if haod is not None:
							s_x, s_y = pyg.center(haod)
							self.dianji(s_x, s_y)  # 点击好
						if fckn is not None:
							s_x, s_y = pyg.center(fckn)
							self.dianji(s_x, s_y)  # 点击非常困难
						if kn is not None:
							s_x, s_y = pyg.center(kn)
							self.dianji(s_x, s_y)  # 点击困难
						if zdui is not None:
							s_x, s_y = pyg.center(zdui)
							self.dianji(s_x, s_y)  # 点击组队决斗
						if cl is not None:
							s_x, s_y = pyg.center(cl)
							self.dianji(s_x, s_y)  # 点击clear
						if gb is not None:
							s_x, s_y = pyg.center(gb)
							self.dianji(s_x, s_y)  # 点击关闭

			if haod is not None:
				s_x, s_y = pyg.center(haod)
				self.dianji(s_x, s_y)  # 点击好
			if cs is not None:
				s_x, s_y = pyg.center(cs)
				self.dianji(s_x, s_y)  # 点击重试
			if fhui is not None:
				s_x, s_y = pyg.center(fhui)
				self.dianji(s_x, s_y)
				time.sleep(1)
				fhui2 = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
				if fhui2 is not None:
					s_x, s_y = pyg.center(fhui2)
					self.dianji(s_x, s_y)  # 点击返回
					time.sleep(1)


'''if __name__ == "__main__":
	WindowsName = u'Yu-Gi-Oh! DUEL LINKS'  # steam
	while True:
		ulist = []
		print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
		ulist.append([" ", "1、pvpKC杯自杀", " "])
		ulist.append([" ", "2、pvp排名决斗自杀", " "])
		ulist.append([" ", "3、pvp休闲决斗自杀", " "])
		ulist.append([" ", "4、自动十级门     ", " "])
		ulist.append([" ", "5、pvp休闲决斗战斗  ", " "])
		ulist.append([" ", "6、pvp排名决斗战斗  ", " "])
		ulist.append([" ", "7、活动组队决斗全自动(已过期)  ", " "])
		for ul in ulist:
			print("{0:^2}\t{1:{3}^9}\t{2:^2}".format(ul[0], ul[1], ul[2], chr(12288)))
			if ul != ulist[-1]:
				print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
		print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
		print("请输入要选择的功能前面的数字并回车.....")
		input1 = str(input(""))
		if input1 == '1' or input1 == '2' or input1 == '3':
			demo = Steam(WindowsName)
			demo.pvp_tolose_steam(input1)
		elif input1 == '4':
			demo = Steam(WindowsName)
			demo.chuansongmen_steam()
		elif input1 == '5':
			demo = Steam(WindowsName)
			demo.pvp_xiuxian_towin_steam()
		elif input1 == '6':
			demo = Steam(WindowsName)
			demo.pvp_paimin_towin_steam()
		elif input1 == '7':
			demo = Steam(WindowsName)
			demo.huodong_zuidui_steam()
		else:
			print("!!!!!输入有误,请重新输入!!!!!")
			time.sleep(1)'''
