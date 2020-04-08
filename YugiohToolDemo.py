#!/usr/bin/python
# coding:utf-8

"""
@author: zyatom
@contact: 70906346@qq.com
@software: PyCharm
@file: YugiohTool.py
@time: 2019/4/25 20:02
"""
import importlib
import os
import sys
import win32gui
import time
import pyautogui as pyg
import configparser
import logging
import requests
import base64
import msvcrt

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

importlib.reload(sys)

logger = logging.getLogger()  # 不加名称设置root logger
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
	'%(asctime)s - %(name)s - %(levelname)s: - %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S')
fh = logging.FileHandler('log.txt')  # 使用FileHandler输出到文件
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
ch = logging.StreamHandler()  # 使用StreamHandler输出到屏幕
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)  # 添加两个Handler
logger.addHandler(fh)
logging.getLogger("urllib3.connectionpool").setLevel(logging.WARNING)  # 设置requests不输出日志
tuisong_time = None


class Networkerror(RuntimeError):
	def __init__(self, arg):
		self.args = arg


class GameAssist:
	def __init__(self, wdname):  # 初始化
		self.hwnd = win32gui.FindWindow(0, wdname)  # 取得窗口句柄
		if not self.hwnd:
			print("窗口找不到，请确认窗口句柄名称：【%s】" % wdname)
			exit()
		win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
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
		tmp.close()

		print("使用前请务必先阅读'脚本使用方法.docx'")
		print("当前版本为试用版，挂机30分钟后停止脚本，继续试用请重新打开本脚本")
		print("如果试用满意可以购买完整版解除限制，欢迎联系我购买（企鹅号70906346）")
		print("有任何脚本功能上的问题或者建议也请联系我")
		print("要关闭脚本请把鼠标放到屏幕左上角停留2秒钟")

	# print("窗口位置：", size)

	@staticmethod
	def tuisong(cishu, text, serviceapi):
		api = serviceapi
		title = "脚本运行" + str(cishu) + "次" + "，" + text
		content = text
		data = {
			"text": title,
			"desp": content
		}
		requests.post(api, data=data)
		logger.info("推送到手机")

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

	def pvp(self):  # pvp
		global tuisong_time
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
			self.dianji(topx + 10, topy + 860)
			jd = pyg.locateOnScreen('YugiohTool/api-jd.dll', confidence=0.60, grayscale=True)
			haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
			cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80, grayscale=True)
			xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
			# qr = pyg.locateOnScreen('YugiohTool/api-qr.dll', confidence=0.80, grayscale=True)
			cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)

			if cs is not None:
				poscs = cs
				s_x, s_y = pyg.center(poscs)
				self.dianji(s_x, s_y)  # 点击重试
				logger.info('无网络>重试')

			if jd is not None:
				posjd = jd
				s_x, s_y = pyg.center(posjd)
				# time.sleep(1)
				self.dianji(s_x, s_y)  # 点击决斗
				count = count + 1
				cf.set('config', 'count', str(count))
				cf.write(open("config.ini", 'w'))  # 写入count次数
				filename = "config.ini"  # 监控配置文件改动
				info = os.stat(filename)
				logger.info('决斗！已对战%s次', str(count))
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
						logger.info('无网络>重试')
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
							# logger.info('菜单')
							time.sleep(0.5)
							js = pyg.locateOnScreen('YugiohTool/api-js.dll', confidence=0.80, grayscale=True)
							if js is not None:
								posjs = js
								s_x, s_y = pyg.center(posjs)
								self.dianji(s_x, s_y)  # 点击结束回合
								# logger.info('结束回合')
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
				# logger.info('菜单')
				time.sleep(0.5)
				js = pyg.locateOnScreen('YugiohTool/api-js.dll', confidence=0.80, grayscale=True)
				if js is not None:
					posjs = js
					s_x, s_y = pyg.center(posjs)
					self.dianji(s_x, s_y)  # 点击结束回合
					logger.info('结束回合')
					time.sleep(1)
					pyg.press('f2')  # 点击多任务键
					time.sleep(32)
					pyg.press('f2')  # 点击多任务键
			'''if qr is not None:
				self.dianji(topx + 100, topy + 670)
				time.sleep(0.2)
				self.dianji(topx + 300, topy + 670)
				time.sleep(0.2)
				self.dianji(topx + 270, topy + 837)  # 点击确认
				logger.info('确认')'''
			if haod is not None:
				poshaod = haod
				s_x, s_y = pyg.center(poshaod)
				self.dianji(s_x, s_y)  # 点击好
			# logger.info('好')
			if xyb is not None:
				posxyb = xyb
				s_x, s_y = pyg.center(posxyb)
				self.dianji(s_x, s_y)  # 点击下一步
			# logger.info('下一步')
			# 每10分钟检测一次
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
				print("试用时间已到，请购买完整版或重启继续试用（按任意键退出...）")
				while True:
					pressedkey = msvcrt.getch()
					if pressedkey is not None:
						exit()

	def chuansongmen(self):  # 十级门
		# e = Networkerror
		global tuisong_time
		cf = configparser.ConfigParser()
		cf.read("config.ini")  # 读取配置文件
		csmcount = int(cf.get("config", "csmcount"))
		start_count = csmcount
		start_time = time.time()
		serviceapi = cf.get("config", "serviceapi")
		# filename = "config.ini"  # 监控配置文件改动
		# info = os.stat(filename)
		size = win32gui.GetWindowRect(self.hwnd)
		topx, topy = size[0], size[1]
		while True:
			time.sleep(0.5)
			self.dianji(topx + 10, topy + 730)
			zjm = pyg.locateOnScreen('YugiohTool/api-zjm.dll', confidence=0.60, grayscale=True)
			haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
			xyb = pyg.locateOnScreen('YugiohTool/api-xyb.dll', confidence=0.80, grayscale=True)
			cs = pyg.locateOnScreen('YugiohTool/api-cs.dll', confidence=0.80, grayscale=True)
			if zjm is not None:
				# poszjm = zjm
				# s_x, s_y = pyg.center(poscs)
				self.dianji(topx + 90, topy + 960)
				time.sleep(0.5)
				self.dianji(topx + 90, topy + 960)
				csmcount = csmcount + 1
				cf.set('config', 'csmcount', str(csmcount))
				cf.write(open("config.ini", 'w'))  # 写入count次数
				filename = "config.ini"  # 监控配置文件改动
				info = os.stat(filename)
				logger.info('第%s次传送门>>>>>>', str(csmcount))
				huihecount = 1
				for i in range(25):
					time.sleep(0.3)
					sjd = pyg.locateOnScreen('YugiohTool/api-sjd.dll', confidence=0.80, grayscale=True)
					if sjd is not None:
						self.dianji(topx + 90, topy + 690)  # 点击等级:10
						possjd = sjd
						s_x, s_y = pyg.center(possjd)
						self.dianji(s_x, s_y)  # 点击决斗
						break
				for i in range(25):
					time.sleep(0.5)
					self.dianji(topx + 10, topy + 860)
					sjd = pyg.locateOnScreen('YugiohTool/api-sjd.dll', confidence=0.80, grayscale=True)
					if sjd is not None:
						possjd = sjd
						s_x, s_y = pyg.center(possjd)
						self.dianji(s_x, s_y)  # 点击决斗
						# logger.info('决斗')
						break
				try:
					for i in range(100):
						gongjicount = 0
						time.sleep(0.5)
						self.dianji(topx + 10, topy + 860)
						cd = pyg.locateOnScreen('YugiohTool/api-cd.dll', confidence=0.80, grayscale=True)
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
								# logger.info('战斗阶段')
								time.sleep(0.5)
								for x in range(25):
									time.sleep(0.3)
									ls = pyg.locateOnScreen('YugiohTool/api-ls.dll', confidence=0.80, grayscale=False)
									haod = pyg.locateOnScreen('YugiohTool/api-h.dll', confidence=0.80, grayscale=True)
									if ls is not None:
										posls = ls
										ls_x, ls_y = pyg.center(posls)
										self.tuodong(ls_x, ls_y)  # 拖动攻击
										gongjicount = gongjicount + 1
										time.sleep(2)
									if haod is not None:
										poshaod = haod
										haod_x, haod_y = pyg.center(poshaod)
										self.dianji(haod_x, haod_y)  # 点击好
										# logger.info('好')
										raise Networkerror("Bad hostname")
									if gongjicount >= huihecount or gongjicount == 3:
										time.sleep(2)
										break
								self.dianji(topx + 490, topy + 630)  # 点击菜单
								time.sleep(1)
								self.dianji(topx + 420, topy + 680)  # 点击回合结束
								huihecount = huihecount + 1
							# break
							else:
								self.dianji(topx + 400, topy + 680)  # 点击结束回合
								huihecount = huihecount + 1
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
				except Networkerror:
					pass

			if haod is not None:
				poshaod = haod
				s_x, s_y = pyg.center(poshaod)
				self.dianji(s_x, s_y)  # 点击好
			# logger.info('好')
			if xyb is not None:
				posxyb = xyb
				s_x, s_y = pyg.center(posxyb)
				self.dianji(s_x, s_y)  # 点击下一步
			# logger.info('下一步')
			if cs is not None:
				poscs = cs
				s_x, s_y = pyg.center(poscs)
				self.dianji(s_x, s_y)  # 点击重试
			# logger.info('无网络>重试')

			'''else:
				 fhui = pyg.locateOnScreen('YugiohTool/api-fh.dll', confidence=0.60, grayscale=True)
				 if fhui is not None:   
					 posfhui = fhui
					 s_x, s_y = pyg.center(posfhui)
					 self.dianji(s_x, s_y)
					 logger.info('返回>>>>>>')'''


if __name__ == "__main__":
	# WindowsName = u'Yu-Gi-Oh! DUEL LINKS'
	WindowsName = u'雷电模拟器'
	# WindowsName = u'BlueStacks App Player'
	demo = GameAssist(WindowsName)
	demo.chuansongmen()
