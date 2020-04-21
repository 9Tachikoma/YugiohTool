# !/usr/bin/python
# coding:utf-8

"""
@author: zyatom
@contact: 70906346@qq.com
@software: PyCharm
@file: YugiohTool.py
@time: 2019/4/25 20:02
"""
import importlib
import msvcrt
import os
import sys
import win32api
import win32gui
import time
import pyautogui as pyg
import configparser
import logging
import requests
import base64

from CaiDan_png import img as caidan
from Chongshi_png import img as chongshi
from duorenwu_png import img as duorenwu
from Hao_png import img as hao
from Jieshu_png import img as jiesu
from JueDou_png import img as juedou
from QueRen_png import img as queren
from XiaYiBu_png import img as xiayibu
from zhongduan_png import img as zhongduan
from zhujiemian_png import img as zhujiemian
from fanhui_png import img as fanhui
from lvse_png import img as lvse
from zhandou_png import img as zhandou
from shijuedou_png import img as shijuedou
from kc_png import img as kcb
from paiming_png import img as paimin
from xiuxian_png import img as xiuxian

from kunnan_png import img as kunnan
from zidongjuedou_png import img as zidongjuedou
from zudui_png import img as zudui

importlib.reload(sys)


def _async_raise(tid, exctype):  # 关闭线程
	tid = ctypes.c_long(tid)
	if not inspect.isclass(exctype):
		exctype = type(exctype)
	res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
	if res == 0:
		raise ValueError("invalid thread id")
	elif res != 1:
		ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
		raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):  # 关闭线程
	_async_raise(thread.ident, SystemExit)

		win32api.keybd_event(13, 0, 0, 0)  #
		self.hwnd = win32gui.FindWindow(0, wdname)  # 取得窗口句柄
		if not self.hwnd:
			print("窗口找不到，请打开【%s】" % wdname)

			exit()
		# win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
		# size = win32gui.GetWindowRect(self.hwnd)
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
		tmp.close()
		first_list = []
		print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
		first_list.append([" ", "试用版脚本交流群819827842", " "])
		first_list.append([" ", "使用前请务必先阅读'脚本使用方法.docx' ", " "])
		first_list.append([" ", "当前版本为试用版，挂机三十分钟后停止，继续试用请重新打开脚本", " "])
		first_list.append([" ", "★★★★★要关闭脚本请把鼠标放到屏幕左上角停留2秒钟★★★★★", " "])
		for f_ul in first_list:
			print("{0:^2}\t{1:{3}^5}\t{2:^2}".format(f_ul[0], f_ul[1], f_ul[2], chr(12288)))
			if f_ul != first_list[-1]:
				print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
		print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")

	def tuisong(self, cishu, text, serviceapi):  # 推送到手机
		api = serviceapi
		title = "脚本运行" + str(cishu) + "次" + "，" + text
		content = text
		data = {
			"text": title,
			"desp": content
		}
		requests.post(api, data=data)
		self.logger.info("推送到手机")

	@staticmethod
	def dianji(x, y):
		pyg.moveTo(x, y)
		time.sleep(0.2)
		pyg.mouseDown()
		pyg.mouseUp()

	@staticmethod
	def tuodong(x, y):
		pyg.moveTo(x, y + 50)
		time.sleep(0.2)
		pyg.dragRel(0, -200, 0.2)

	def pvp_tolose(self, arg):  # pvp自杀
		win32api.keybd_event(13, 0, 0, 0)  #
		win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
		global tuisong_time
		mode = None
		cf = configparser.ConfigParser()
		cf.read("config.ini")  # 读取配置文件
		count = int(cf.get("config", "count"))
		start_count = count
		start_time = time.time()
		serviceapi = cf.get("config", "serviceapi")
		filename = "config.ini"  # 监控配置文件改动
		info = os.stat(filename)
		size = win32gui.GetWindowRect(self.hwnd)
		topx, topy = size[0], size[1]
		while True:
			time.sleep(0.5)
			self.dianji(topx + 315, topy + 90)
			zjm = pyg.locateOnScreen('YugiohTool/api-zjm.dll', confidence=0.60, grayscale=True)
			haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
			xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
			cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
			fhui = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
			if zjm is not None:
				self.dianji(topx + 210, topy + 960)  # 点击pvp门固定点
				time.sleep(2)
				kc = pyg.locateOnScreen('YugiohTool/api-kc.dll', confidence=0.80, grayscale=True)
				pm = pyg.locateOnScreen('YugiohTool/api-pm.dll', confidence=0.80, grayscale=True)
				if str(arg) == '1':
					mode = kc
				elif str(arg) == '2':
					mode = pm
				elif str(arg) == '3':
					self.tuodong(topx + 230, topy + 870)
					time.sleep(2)
					xx = pyg.locateOnScreen('YugiohTool/api-xx.dll', confidence=0.80, grayscale=True)
					mode = xx

				if mode is not None:
					mode = mode
					s_x, s_y = pyg.center(mode)
					self.dianji(s_x, s_y)  # 点击决斗模式
					time.sleep(2)
					while True:
						time.sleep(0.5)
						self.dianji(topx + 10, topy + 860)
						jd = pyg.locateOnScreen('YugiohTool/api-jd.dll', confidence=0.60, grayscale=True)
						haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
						cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80, grayscale=True)
						xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
						qr = pyg.locateOnScreen('YugiohTool/api-qr.dll', confidence=0.80, grayscale=True)
						cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)

						if cs is not None:
							poscs = cs
							s_x, s_y = pyg.center(poscs)
							self.dianji(s_x, s_y)  # 点击重试

						if jd is not None:
							posjd = jd
							s_x, s_y = pyg.center(posjd)
							self.dianji(s_x, s_y)  # 点击决斗
							count = count + 1
							cf.set('config', 'count', str(count))
							cf.write(open("config.ini", 'w'))  # 写入count次数
							filename = "config.ini"  # 监控配置文件改动
							info = os.stat(filename)
							self.logger.info('决斗！已对战%s次', str(count))
							for i in range(25):
								time.sleep(0.3)
								self.dianji(s_x, s_y)
								zd = pyg.locateOnScreen('YugiohTool/api-zd.dll', confidence=0.80, grayscale=True)
								if zd is not None:
									break
								cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
								if cs is not None:
									poscs = cs
									s_x, s_y = pyg.center(poscs)
									self.dianji(s_x, s_y)  # 点击重试
							for i in range(50):
								time.sleep(0.5)
								self.dianji(topx + 10, topy + 860)
								drw = pyg.locateOnScreen('YugiohTool/api-drw.dll', confidence=0.80, grayscale=True)
								if drw is not None:
									time.sleep(3)
									cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80, grayscale=True)
									if cd is not None:
										poscd = cd
										s_x, s_y = pyg.center(poscd)
										self.dianji(s_x, s_y)  # 点击菜单
										time.sleep(0.5)
										js = pyg.locateOnScreen('YugiohTool/api-js.dll', confidence=0.80,
										                        grayscale=True)
										if js is not None:
											posjs = js
											s_x, s_y = pyg.center(posjs)
											self.dianji(s_x, s_y)  # 点击结束回合
											time.sleep(1)
											pyg.press('f2')  # 点击多任务键
											time.sleep(32)
											pyg.press('f2')  # 点击多任务键
											time.sleep(2)
											break
									else:
										pyg.press('f2')  # 点击多任务键
										time.sleep(32)
										pyg.press('f2')  # 点击多任务键
										break
						if cd is not None:
							poscd = cd
							s_x, s_y = pyg.center(poscd)
							self.dianji(s_x, s_y)  # 点击菜单
							time.sleep(0.5)
							js = pyg.locateOnScreen('YugiohTool/api-js.dll', confidence=0.80, grayscale=True)
							if js is not None:
								posjs = js
								s_x, s_y = pyg.center(posjs)
								self.dianji(s_x, s_y)  # 点击结束回合
								time.sleep(1)
								pyg.press('f2')  # 点击多任务键
								time.sleep(32)
								pyg.press('f2')  # 点击多任务键
						if qr is not None:
							posqr = qr
							s_x, s_y = pyg.center(posqr)
							self.dianji(topx + 100, topy + 670)
							time.sleep(0.2)
							self.dianji(topx + 300, topy + 670)
							time.sleep(0.2)
							self.dianji(s_x, s_y)  # 点击确认
						if haod is not None:
							poshaod = haod
							s_x, s_y = pyg.center(poshaod)
							self.dianji(s_x, s_y)  # 点击好
						if xyb is not None:
							posxyb = xyb
							s_x, s_y = pyg.center(posxyb)
							self.dianji(s_x, s_y)  # 点击下一步
						# 每10分钟检测一次
						if int(str(time.localtime().tm_min)[-1]) is 0:
							# 文件没有改动超过10分钟且运行时间超过10分钟微信推送提醒
							if time.time() - info.st_mtime > 600 and time.time() - start_time > 600:
								if tuisong_time is None or time.time() - tuisong_time > 600:
									count_per_hour = count - start_count
									self.tuisong(count_per_hour, "脚本异常停止！", serviceapi)
									tuisong_time = time.time()
									break
							# 整点发送推送
							if int(str(time.localtime().tm_min)) == 00:
								if time.time() - info.st_mtime < 600:
									if tuisong_time is None or time.time() - tuisong_time > 600:
										count_per_hour = count - start_count
										start_count = count
										self.tuisong(count_per_hour, "一切正常！", serviceapi)
										tuisong_time = time.time()
						if time.time() - start_time > 1800:
							self.logger.info('试用时间已到，请购买完整版或重启继续试用（按任意键退出...）')
							while True:
								pressedkey = msvcrt.getch()
								if pressedkey is not None:
									exit()
			if haod is not None:
				poshaod = haod
				s_x, s_y = pyg.center(poshaod)
				self.dianji(s_x, s_y)  # 点击好
				time.sleep(1)
			# self.dianji(topx + 10, topy + 730)
			if xyb is not None:
				posxyb = xyb
				s_x, s_y = pyg.center(posxyb)
				self.dianji(s_x, s_y)  # 点击下一步
				time.sleep(1)
			# self.dianji(topx + 10, topy + 730)
			if cs is not None:
				poscs = cs
				s_x, s_y = pyg.center(poscs)
				self.dianji(s_x, s_y)  # 点击重试
			if fhui is not None:
				posfhui = fhui
				s_x, s_y = pyg.center(posfhui)
				self.dianji(s_x, s_y)  # 点击返回
				time.sleep(1)
				fhui2 = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
				if fhui2 is not None:
					posfhui2 = fhui2
					s_x, s_y = pyg.center(posfhui2)
					self.dianji(s_x, s_y)  # 点击返回
					time.sleep(1)

	def chuansongmen(self):  # 十级门
		win32api.keybd_event(13, 0, 0, 0)  #
		win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
		global tuisong_time
		cf = configparser.ConfigParser()
		cf.read("config.ini")  # 读取配置文件
		csmcount = int(cf.get("config", "csmcount"))
		start_count = csmcount
		start_time = time.time()
		serviceapi = cf.get("config", "serviceapi")
		size = win32gui.GetWindowRect(self.hwnd)
		topx, topy = size[0], size[1]
		while True:
			time.sleep(0.5)
			self.dianji(topx + 315, topy + 90)
			zjm = pyg.locateOnScreen('YugiohTool/api-zjm.dll', confidence=0.60, grayscale=True)
			haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
			xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
			cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
			fhui = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
			if zjm is not None:
				self.dianji(topx + 90, topy + 960)  # 点击传送门固定点
				time.sleep(2)
				sjd = pyg.locateOnScreen('YugiohTool/api-sjd.dll', confidence=0.80, grayscale=True)
				time.sleep(0.3)
				if sjd is not None:
					self.dianji(topx + 90, topy + 690)  # 点击等级:10
					possjd = sjd
					s_x, s_y = pyg.center(possjd)
					self.dianji(s_x, s_y)  # 点击决斗
					for i in range(25):
						time.sleep(0.5)
						self.dianji(topx + 315, topy + 90)
						sjd = pyg.locateOnScreen('YugiohTool/api-sjd.dll', confidence=0.80, grayscale=True)
						if sjd is not None:
							possjd = sjd
							s_x, s_y = pyg.center(possjd)
							self.dianji(s_x, s_y)  # 点击决斗
							csmcount = csmcount + 1
							cf.set('config', 'csmcount', str(csmcount))
							cf.write(open("config.ini", 'w'))  # 写入count次数
							filename = "config.ini"  # 监控配置文件改动
							info = os.stat(filename)
							self.logger.info('第%s次传送门>>>>>>', str(csmcount))
							huihecount = 1
							break
					try:
						for i in range(100):
							gongjicount = 0
							time.sleep(0.5)
							self.dianji(topx + 10, topy + 860)
							cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80, grayscale=True)
							haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
							if cd is not None:
								self.tuodong(topx + 230, topy + 870)  # 拖动卡牌
								time.sleep(0.5)
								self.dianji(topx + 200, topy + 750)  # 点击通常召唤
								time.sleep(2)
								self.dianji(topx + 490, topy + 650)  # 点击菜单
								time.sleep(1)
								zdu = pyg.locateOnScreen('YugiohTool/api-zdu.dll', confidence=0.80, grayscale=True)
								if zdu is not None:
									poszdu = zdu
									zdu_x, zdu_y = pyg.center(poszdu)
									self.dianji(zdu_x, zdu_y)  # 点击战斗
									time.sleep(0.5)
									for x in range(25):
										time.sleep(0.3)
										ls = pyg.locateOnScreen('YugiohTool/api-ls.dll', confidence=0.80,
										                        grayscale=False)
										haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80,
										                          grayscale=True)
										if ls is not None:
											posls = ls
											ls_x, ls_y = pyg.center(posls)
											self.tuodong(ls_x, ls_y)  # 拖动攻击
											gongjicount = gongjicount + 1
											time.sleep(1)
										if haod is not None:
											poshaod = haod
											haod_x, haod_y = pyg.center(poshaod)
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
													poscd = cd
													s_x, s_y = pyg.center(poscd)
													self.dianji(s_x, s_y)  # 点击菜单
													time.sleep(0.5)
													js = pyg.locateOnScreen('YugiohTool/api-js.dll', confidence=0.80,
													                        grayscale=True)
													if js is not None:
														posjs = js
														s_x, s_y = pyg.center(posjs)
														self.dianji(s_x, s_y)  # 点击结束回合
														huihecount = huihecount + 1
														time.sleep(1)
														break
											break
								else:
									self.dianji(topx + 400, topy + 680)  # 点击结束回合
									huihecount = huihecount + 1
							if haod is not None:
								poshaod = haod
								haod_x, haod_y = pyg.center(poshaod)
								self.dianji(haod_x, haod_y)  # 点击好
								raise Networkerror("Bad hostname")
							if int(str(time.localtime().tm_min)[-1]) is 0:
								# 文件没有改动超过10分钟且运行时间超过10分钟微信推送提醒
								if time.time() - info.st_mtime > 600 and time.time() - start_time > 600:
									if tuisong_time is None or time.time() - tuisong_time > 600:
										count_per_hour = csmcount - start_count
										self.tuisong(count_per_hour, "脚本异常停止！", serviceapi)
										tuisong_time = time.time()
								# 整点发送推送
								if int(str(time.localtime().tm_min)) == 00:
									if time.time() - info.st_mtime < 600:
										if tuisong_time is None or time.time() - tuisong_time > 600:
											count_per_hour = csmcount - start_count
											start_count = csmcount
											self.tuisong(count_per_hour, "一切正常！", serviceapi)
											tuisong_time = time.time()
							if time.time() - start_time > 1800:
								self.logger.info('试用时间已到，请购买完整版或重启继续试用（按任意键退出...）')
								while True:
									pressedkey = msvcrt.getch()
									if pressedkey is not None:
										exit()
					except Networkerror:
						pass

			if haod is not None:
				poshaod = haod
				s_x, s_y = pyg.center(poshaod)
				self.dianji(s_x, s_y)  # 点击好
			if xyb is not None:
				posxyb = xyb
				s_x, s_y = pyg.center(posxyb)
				self.dianji(s_x, s_y)  # 点击下一步
			if cs is not None:
				poscs = cs
				s_x, s_y = pyg.center(poscs)
				self.dianji(s_x, s_y)  # 点击重试
			if fhui is not None:
				posfhui = fhui
				s_x, s_y = pyg.center(posfhui)
				self.dianji(s_x, s_y)
				time.sleep(1)
				fhui2 = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
				if fhui2 is not None:
					posfhui2 = fhui2
					s_x, s_y = pyg.center(posfhui2)
					self.dianji(s_x, s_y)  # 点击返回
					time.sleep(1)

	def pvp_xiuxian_towin(self):  # pvp休闲towin
		win32api.keybd_event(13, 0, 0, 0)  #
		win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
		global tuisong_time
		# mode = None
		cf = configparser.ConfigParser()
		cf.read("config.ini")  # 读取配置文件
		count = int(cf.get("config", "count"))
		start_count = count
		start_time = time.time()
		serviceapi = cf.get("config", "serviceapi")
		filename = "config.ini"  # 监控配置文件改动
		info = os.stat(filename)
		size = win32gui.GetWindowRect(self.hwnd)
		topx, topy = size[0], size[1]
		while True:
			time.sleep(0.5)
			zjm = pyg.locateOnScreen('YugiohTool/api-zjm.dll', confidence=0.60, grayscale=True)
			haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
			xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
			cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
			fhui = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
			if zjm is not None:
				self.dianji(topx + 210, topy + 960)  # 点击pvp门固定点
				time.sleep(2)
				self.tuodong(topx + 230, topy + 870)
				time.sleep(2)
				xx = pyg.locateOnScreen('YugiohTool/api-xx.dll', confidence=0.80, grayscale=True)
				time.sleep(1)
				if xx is not None:
					posxx = xx
					s_x, s_y = pyg.center(posxx)
					self.dianji(s_x, s_y)  # 点击休闲
					time.sleep(2)
					while True:
						time.sleep(0.5)
						self.dianji(topx + 315, topy + 90)
						jd = pyg.locateOnScreen('YugiohTool/api-jd.dll', confidence=0.60, grayscale=True)
						haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
						# cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80, grayscale=True)
						xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
						qr = pyg.locateOnScreen('YugiohTool/api-qr.dll', confidence=0.80, grayscale=True)
						cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
						huihecount = 1
						if cs is not None:
							poscs = cs
							s_x, s_y = pyg.center(poscs)
							self.dianji(s_x, s_y)  # 点击重试

						if jd is not None:
							posjd = jd
							s_x, s_y = pyg.center(posjd)
							self.dianji(s_x, s_y)  # 点击决斗
							count = count + 1
							cf.set('config', 'count', str(count))
							cf.write(open("config.ini", 'w'))  # 写入count次数
							filename = "config.ini"  # 监控配置文件改动
							info = os.stat(filename)
							self.logger.info('决斗！已对战%s次', str(count))
							for i in range(25):
								time.sleep(0.3)
								self.dianji(s_x, s_y)
								zd = pyg.locateOnScreen('YugiohTool/api-zd.dll', confidence=0.80, grayscale=True)
								if zd is not None:
									break
								cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
								if cs is not None:
									poscs = cs
									s_x, s_y = pyg.center(poscs)
									self.dianji(s_x, s_y)  # 点击重试
							try:
								a = 0
								while a < 150:
									gongjicount = 0
									time.sleep(0.5)
									self.dianji(topx + 10, topy + 860)
									cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80, grayscale=True)
									haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
									a = a + 1
									if cd is not None:
										a = 1
										self.tuodong(topx + 230, topy + 870)  # 拖动卡牌
										time.sleep(0.5)
										self.dianji(topx + 200, topy + 750)  # 点击通常召唤
										time.sleep(2)

										for k in range(100):  # 等菜单
											time.sleep(0.5)
											cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80,
											                        grayscale=True)
											if cd is not None:
												poscd = cd
												s_x, s_y = pyg.center(poscd)
												self.dianji(s_x, s_y)  # 点击菜单
												break
										time.sleep(1)
										zdu = pyg.locateOnScreen('YugiohTool/api-zdu.dll', confidence=0.80,
										                         grayscale=True)
										if zdu is not None:
											poszdu = zdu
											zdu_x, zdu_y = pyg.center(poszdu)
											self.dianji(zdu_x, zdu_y)  # 点击战斗
											time.sleep(0.5)
											try:
												for h in range(100):  # 等菜单
													time.sleep(0.5)
													cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80,
													                        grayscale=True)

													if cd is not None:
														for g in range(50):  # 等菜单
															time.sleep(0.5)
															lvs = pyg.locateOnScreen('YugiohTool/api-ls.dll',
															                         confidence=0.80,
															                         grayscale=False)
															haod = pyg.locateOnScreen('YugiohTool/api-h.dll',
															                          confidence=0.80,
															                          grayscale=True)
															if lvs is not None:
																posls = lvs
																ls_x, ls_y = pyg.center(posls)
																self.tuodong(ls_x, ls_y)  # 拖动攻击
																gongjicount = gongjicount + 1
																time.sleep(1)
															if haod is not None:
																poshaod = haod
																haod_x, haod_y = pyg.center(poshaod)
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
																		poscd = cd
																		s_x, s_y = pyg.center(poscd)
																		self.dianji(s_x, s_y)  # 点击菜单
																		time.sleep(0.5)
																		js = pyg.locateOnScreen('YugiohTool/api-js.dll',
																		                        confidence=0.80,
																		                        grayscale=True)
																		if js is not None:
																			posjs = js
																			s_x, s_y = pyg.center(posjs)
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
																		poscd = cd
																		s_x, s_y = pyg.center(poscd)
																		self.dianji(s_x, s_y)  # 点击菜单
																		time.sleep(0.5)
																		js = pyg.locateOnScreen('YugiohTool/api-js.dll',
																		                        confidence=0.80,
																		                        grayscale=True)
																		if js is not None:
																			posjs = js
																			s_x, s_y = pyg.center(posjs)
																			self.dianji(s_x, s_y)  # 点击结束回合
																			huihecount = huihecount + 1
																			time.sleep(1)
																			raise StopIteration("Bad hostname")
											except StopIteration:
												pass
										else:
											self.dianji(topx + 400, topy + 680)  # 点击结束回合
											huihecount = huihecount + 1
									if haod is not None:
										poshaod = haod
										haod_x, haod_y = pyg.center(poshaod)
										self.dianji(haod_x, haod_y)  # 点击好
										raise Networkerror("Bad hostname")
									if int(str(time.localtime().tm_min)[-1]) is 0:
										# 文件没有改动超过10分钟且运行时间超过10分钟微信推送提醒
										if time.time() - info.st_mtime > 600 and time.time() - start_time > 600:
											if tuisong_time is None or time.time() - tuisong_time > 600:
												count_per_hour = count - start_count
												self.tuisong(count_per_hour, "脚本异常停止！", serviceapi)
												tuisong_time = time.time()
										# 整点发送推送
										if int(str(time.localtime().tm_min)) == 00:
											if time.time() - info.st_mtime < 600:
												if tuisong_time is None or time.time() - tuisong_time > 600:
													count_per_hour = count - start_count
													start_count = count
													self.tuisong(count_per_hour, "一切正常！", serviceapi)
													tuisong_time = time.time()
									if time.time() - start_time > 1800:
										self.logger.info('试用时间已到，请购买完整版或重启继续试用（按任意键退出...）')
										while True:
											pressedkey = msvcrt.getch()
											if pressedkey is not None:
												exit()
							except Networkerror:
								pass
						if qr is not None:
							posqr = qr
							self.dianji(s_x, s_y)  # 点击菜单
							self.dianji(topx + 100, topy + 670)
							time.sleep(0.2)
							self.dianji(topx + 300, topy + 670)
							time.sleep(0.2)
							s_x, s_y = pyg.center(posqr)
						# self.dianji(topx + 270, topy + 837)  # 点击确认
						if haod is not None:
							poshaod = haod
							s_x, s_y = pyg.center(poshaod)
							self.dianji(s_x, s_y)  # 点击好
						if xyb is not None:
							posxyb = xyb
							s_x, s_y = pyg.center(posxyb)
							self.dianji(s_x, s_y)  # 点击下一步
						# 每10分钟检测一次
						if int(str(time.localtime().tm_min)[-1]) is 0:
							# 文件没有改动超过10分钟且运行时间超过10分钟微信推送提醒
							if time.time() - info.st_mtime > 600 and time.time() - start_time > 600:
								if tuisong_time is None or time.time() - tuisong_time > 600:
									count_per_hour = count - start_count
									self.tuisong(count_per_hour, "脚本异常停止！", serviceapi)
									tuisong_time = time.time()
									break
							# 整点发送推送
							if int(str(time.localtime().tm_min)) == 00:
								if time.time() - info.st_mtime < 600:
									if tuisong_time is None or time.time() - tuisong_time > 600:
										count_per_hour = count - start_count
										start_count = count
										self.tuisong(count_per_hour, "一切正常！", serviceapi)
										tuisong_time = time.time()
						if time.time() - start_time > 1800:
							self.logger.info('试用时间已到，请购买完整版或重启继续试用（按任意键退出...）')
							while True:
								pressedkey = msvcrt.getch()
								if pressedkey is not None:
									exit()
			if haod is not None:
				poshaod = haod
				s_x, s_y = pyg.center(poshaod)
				self.dianji(s_x, s_y)  # 点击好
				time.sleep(1)
			# self.dianji(topx + 10, topy + 730)
			if xyb is not None:
				posxyb = xyb
				s_x, s_y = pyg.center(posxyb)
				self.dianji(s_x, s_y)  # 点击下一步
				time.sleep(1)
			# self.dianji(topx + 10, topy + 730)
			if cs is not None:
				poscs = cs
				s_x, s_y = pyg.center(poscs)
				self.dianji(s_x, s_y)  # 点击重试
			if fhui is not None:
				posfhui = fhui
				s_x, s_y = pyg.center(posfhui)
				self.dianji(s_x, s_y)  # 点击返回
				time.sleep(1)
				fhui2 = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
				if fhui2 is not None:
					posfhui2 = fhui2
					s_x, s_y = pyg.center(posfhui2)
					self.dianji(s_x, s_y)  # 点击返回
					time.sleep(1)
			self.dianji(topx + 315, topy + 90)

	def pvp_paimin_towin(self):  # pvp休闲towin
		win32api.keybd_event(13, 0, 0, 0)  #
		win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
		global tuisong_time
		# mode = None
		cf = configparser.ConfigParser()
		cf.read("config.ini")  # 读取配置文件
		count = int(cf.get("config", "count"))
		start_count = count
		start_time = time.time()
		serviceapi = cf.get("config", "serviceapi")
		filename = "config.ini"  # 监控配置文件改动
		info = os.stat(filename)
		size = win32gui.GetWindowRect(self.hwnd)
		topx, topy = size[0], size[1]
		while True:
			time.sleep(0.5)
			zjm = pyg.locateOnScreen('YugiohTool/api-zjm.dll', confidence=0.60, grayscale=True)
			haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
			xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
			cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
			fhui = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
			if zjm is not None:
				self.dianji(topx + 210, topy + 960)  # 点击pvp门固定点
				time.sleep(2)
				pm = pyg.locateOnScreen('YugiohTool/api-pm.dll', confidence=0.80, grayscale=True)
				time.sleep(1)
				if pm is not None:
					pospm = pm
					s_x, s_y = pyg.center(pospm)
					self.dianji(s_x, s_y)  # 点击排名
					time.sleep(2)
					while True:
						time.sleep(0.5)
						self.dianji(topx + 315, topy + 90)
						jd = pyg.locateOnScreen('YugiohTool/api-jd.dll', confidence=0.60, grayscale=True)
						haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
						# cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80, grayscale=True)
						xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
						qr = pyg.locateOnScreen('YugiohTool/api-qr.dll', confidence=0.80, grayscale=True)
						cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
						huihecount = 1
						if cs is not None:
							poscs = cs
							s_x, s_y = pyg.center(poscs)
							self.dianji(s_x, s_y)  # 点击重试

						if jd is not None:
							posjd = jd
							s_x, s_y = pyg.center(posjd)
							self.dianji(s_x, s_y)  # 点击决斗
							count = count + 1
							cf.set('config', 'count', str(count))
							cf.write(open("config.ini", 'w'))  # 写入count次数
							filename = "config.ini"  # 监控配置文件改动
							info = os.stat(filename)
							self.logger.info('决斗！已对战%s次', str(count))
							for i in range(25):
								time.sleep(0.3)
								self.dianji(s_x, s_y)
								zd = pyg.locateOnScreen('YugiohTool/api-zd.dll', confidence=0.80, grayscale=True)
								if zd is not None:
									break
								cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
								if cs is not None:
									poscs = cs
									s_x, s_y = pyg.center(poscs)
									self.dianji(s_x, s_y)  # 点击重试
							try:
								a = 0
								while a < 150:
									gongjicount = 0
									time.sleep(0.5)
									self.dianji(topx + 10, topy + 860)
									cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80, grayscale=True)
									haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
									a = a + 1
									if cd is not None:
										a = 1
										self.tuodong(topx + 230, topy + 870)  # 拖动卡牌
										time.sleep(0.5)
										self.dianji(topx + 200, topy + 750)  # 点击通常召唤
										time.sleep(2)

										for k in range(100):  # 等菜单
											time.sleep(0.5)
											cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80,
											                        grayscale=True)
											if cd is not None:
												poscd = cd
												s_x, s_y = pyg.center(poscd)
												self.dianji(s_x, s_y)  # 点击菜单
												break
										time.sleep(1)
										zdu = pyg.locateOnScreen('YugiohTool/api-zdu.dll', confidence=0.80,
										                         grayscale=True)
										if zdu is not None:
											poszdu = zdu
											zdu_x, zdu_y = pyg.center(poszdu)
											self.dianji(zdu_x, zdu_y)  # 点击战斗
											time.sleep(0.5)
											try:
												for h in range(100):  # 等菜单
													time.sleep(0.5)
													cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80,
													                        grayscale=True)

													if cd is not None:
														for g in range(50):  # 等菜单
															time.sleep(0.5)
															lvs = pyg.locateOnScreen('YugiohTool/api-ls.dll',
															                         confidence=0.80,
															                         grayscale=False)
															haod = pyg.locateOnScreen('YugiohTool/api-h.dll',
															                          confidence=0.80,
															                          grayscale=True)
															if lvs is not None:
																posls = lvs
																ls_x, ls_y = pyg.center(posls)
																self.tuodong(ls_x, ls_y)  # 拖动攻击
																gongjicount = gongjicount + 1
																time.sleep(1)
															if haod is not None:
																poshaod = haod
																haod_x, haod_y = pyg.center(poshaod)
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
																		poscd = cd
																		s_x, s_y = pyg.center(poscd)
																		self.dianji(s_x, s_y)  # 点击菜单
																		time.sleep(0.5)
																		js = pyg.locateOnScreen('YugiohTool/api-js.dll',
																		                        confidence=0.80,
																		                        grayscale=True)
																		if js is not None:
																			posjs = js
																			s_x, s_y = pyg.center(posjs)
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
																		poscd = cd
																		s_x, s_y = pyg.center(poscd)
																		self.dianji(s_x, s_y)  # 点击菜单
																		time.sleep(0.5)
																		js = pyg.locateOnScreen('YugiohTool/api-js.dll',
																		                        confidence=0.80,
																		                        grayscale=True)
																		if js is not None:
																			posjs = js
																			s_x, s_y = pyg.center(posjs)
																			self.dianji(s_x, s_y)  # 点击结束回合
																			huihecount = huihecount + 1
																			time.sleep(1)
																			raise StopIteration("Bad hostname")
											except StopIteration:
												pass

										else:
											self.dianji(topx + 400, topy + 680)  # 点击结束回合
											huihecount = huihecount + 1
									if haod is not None:
										poshaod = haod
										haod_x, haod_y = pyg.center(poshaod)
										self.dianji(haod_x, haod_y)  # 点击好
										raise Networkerror("Bad hostname")
									if int(str(time.localtime().tm_min)[-1]) is 0:
										# 文件没有改动超过10分钟且运行时间超过10分钟微信推送提醒
										if time.time() - info.st_mtime > 600 and time.time() - start_time > 600:
											if tuisong_time is None or time.time() - tuisong_time > 600:
												count_per_hour = count - start_count
												self.tuisong(count_per_hour, "脚本异常停止！", serviceapi)
												tuisong_time = time.time()
										# 整点发送推送
										if int(str(time.localtime().tm_min)) == 00:
											if time.time() - info.st_mtime < 600:
												if tuisong_time is None or time.time() - tuisong_time > 600:
													count_per_hour = count - start_count
													start_count = count
													self.tuisong(count_per_hour, "一切正常！", serviceapi)
													tuisong_time = time.time()
									if time.time() - start_time > 1800:
										self.logger.info('试用时间已到，请购买完整版或重启继续试用（按任意键退出...）')
										while True:
											pressedkey = msvcrt.getch()
											if pressedkey is not None:
												exit()
							except Networkerror:
								pass
						if qr is not None:
							posqr = qr
							s_x, s_y = pyg.center(posqr)
							self.dianji(topx + 100, topy + 670)
							time.sleep(0.2)
							self.dianji(topx + 300, topy + 670)
							time.sleep(0.2)
							self.dianji(s_x, s_y)  # 点击确认
						if haod is not None:
							poshaod = haod
							s_x, s_y = pyg.center(poshaod)
							self.dianji(s_x, s_y)  # 点击好
						if xyb is not None:
							posxyb = xyb
							s_x, s_y = pyg.center(posxyb)
							self.dianji(s_x, s_y)  # 点击下一步
						# 每10分钟检测一次
						if int(str(time.localtime().tm_min)[-1]) is 0:
							# 文件没有改动超过10分钟且运行时间超过10分钟微信推送提醒
							if time.time() - info.st_mtime > 600 and time.time() - start_time > 600:
								if tuisong_time is None or time.time() - tuisong_time > 600:
									count_per_hour = count - start_count
									self.tuisong(count_per_hour, "脚本异常停止！", serviceapi)
									tuisong_time = time.time()
									break
							# 整点发送推送
							if int(str(time.localtime().tm_min)) == 00:
								if time.time() - info.st_mtime < 600:
									if tuisong_time is None or time.time() - tuisong_time > 600:
										count_per_hour = count - start_count
										start_count = count
										self.tuisong(count_per_hour, "一切正常！", serviceapi)
										tuisong_time = time.time()
						if time.time() - start_time > 1800:
							self.logger.info('试用时间已到，请购买完整版或重启继续试用（按任意键退出...）')
							while True:
								pressedkey = msvcrt.getch()
								if pressedkey is not None:
									exit()
			if haod is not None:
				poshaod = haod
				s_x, s_y = pyg.center(poshaod)
				self.dianji(s_x, s_y)  # 点击好
				time.sleep(1)
			if xyb is not None:
				posxyb = xyb
				s_x, s_y = pyg.center(posxyb)
				self.dianji(s_x, s_y)  # 点击下一步
				time.sleep(1)
			if cs is not None:
				poscs = cs
				s_x, s_y = pyg.center(poscs)
				self.dianji(s_x, s_y)  # 点击重试
			if fhui is not None:
				posfhui = fhui
				s_x, s_y = pyg.center(posfhui)
				self.dianji(s_x, s_y)  # 点击返回
				time.sleep(1)
				fhui2 = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
				if fhui2 is not None:
					posfhui2 = fhui2
					s_x, s_y = pyg.center(posfhui2)
					self.dianji(s_x, s_y)  # 点击返回
					time.sleep(1)
			self.dianji(topx + 10, topy + 757)

	def huodong_zuidui(self):
		win32api.keybd_event(13, 0, 0, 0)  #
		win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
		global tuisong_time
		start_time = time.time()
		size = win32gui.GetWindowRect(self.hwnd)
		topx, topy = size[0], size[1]
		while True:
			time.sleep(0.5)
			self.dianji(topx + 315, topy + 90)
			zjm = pyg.locateOnScreen('YugiohTool/api-zjm.dll', confidence=0.60, grayscale=True)
			haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
			cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
			fhui = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
			if zjm is not None:
				self.dianji(topx + 190, topy + 890)  # 点击活动固定点
				time.sleep(2)
				zdui = pyg.locateOnScreen('YugiohTool/api-zdui.dll', confidence=0.80, grayscale=True)
				time.sleep(0.3)
				if zdui is not None:
					poszdui = zdui
					s_x, s_y = pyg.center(poszdui)
					self.dianji(s_x, s_y)  # 点击组队决斗
					while True:
						time.sleep(0.3)
						self.dianji(topx + 315, topy + 90)
						zdjd = pyg.locateOnScreen('YugiohTool/api-zdjd.dll', confidence=0.80, grayscale=True)
						kn = pyg.locateOnScreen('YugiohTool/api-kn.dll', confidence=0.80, grayscale=True)
						zdui = pyg.locateOnScreen('YugiohTool/api-zdui.dll', confidence=0.80, grayscale=True)
						haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
						if zdjd is not None:
							poszdjd = zdjd
							s_x, s_y = pyg.center(poszdjd)
							self.dianji(s_x, s_y)  # 点击自动决斗
						if haod is not None:
							poshaod = haod
							s_x, s_y = pyg.center(poshaod)
							self.dianji(s_x, s_y)  # 点击好
						if kn is not None:
							poskn = kn
							s_x, s_y = pyg.center(poskn)
							self.dianji(s_x, s_y)  # 点击困难
						if zdui is not None:
							poszdui = zdui
							s_x, s_y = pyg.center(poszdui)
							self.dianji(s_x, s_y)  # 点击组队决斗
						if time.time() - start_time > 1800:
							self.logger.info('试用时间已到，请购买完整版或重启继续试用（按任意键退出...）')
							while True:
								pressedkey = msvcrt.getch()
								if pressedkey is not None:
									exit()

			if haod is not None:
				poshaod = haod
				s_x, s_y = pyg.center(poshaod)
				self.dianji(s_x, s_y)  # 点击好
			if cs is not None:
				poscs = cs
				s_x, s_y = pyg.center(poscs)
				self.dianji(s_x, s_y)  # 点击重试
			if fhui is not None:
				posfhui = fhui
				s_x, s_y = pyg.center(posfhui)
				self.dianji(s_x, s_y)
				time.sleep(1)
				fhui2 = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.80, grayscale=True)
				if fhui2 is not None:
					posfhui2 = fhui2
					s_x, s_y = pyg.center(posfhui2)
					self.dianji(s_x, s_y)  # 点击返回
					time.sleep(1)

if __name__ == "__main__":
	# WindowsName = u'Yu-Gi-Oh! DUEL LINKS'  # steam
	WindowsName = u'雷电模拟器'
	while True:
		ulist = []
		print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
		ulist.append([" ", "1、pvpKC杯自杀", " "])
		ulist.append([" ", "2、pvp排名决斗自杀", " "])
		ulist.append([" ", "3、pvp休闲决斗自杀", " "])
		ulist.append([" ", "4、自动十级门         ", " "])
		ulist.append([" ", "5、pvp休闲决斗战斗  ", " "])
		ulist.append([" ", "6、pvp排名决斗战斗  ", " "])
		ulist.append([" ", "7、最新活动组队决斗全自动  ", " "])
		for ul in ulist:
			print("{0:^2}\t{1:{3}^9}\t{2:^2}".format(ul[0], ul[1], ul[2], chr(12288)))
			if ul != ulist[-1]:
				print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
		print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
		print("请输入要选择的功能前面的数字并回车.....")
		input1 = str(input(""))
		if input1 == '1' or input1 == '2' or input1 == '3':
			demo = GameAssist(WindowsName)
			demo.pvp_tolose(input1)
		elif input1 == '4':
			demo = GameAssist(WindowsName)
			demo.chuansongmen()
		elif input1 == '5':
			demo = GameAssist(WindowsName)
			demo.pvp_xiuxian_towin()
		elif input1 == '6':
			demo = GameAssist(WindowsName)
			demo.pvp_paimin_towin()
		elif input1 == '7':
			demo = GameAssist(WindowsName)
			demo.huodong_zuidui()
		else:
			print("!!!!!输入有误,请重新输入!!!!!")
			time.sleep(1)
