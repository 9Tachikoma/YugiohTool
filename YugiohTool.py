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


class GameAssist:
	def __init__(self, wdname):  # 初始化
		self.hwnd = win32gui.FindWindow(0, wdname)  # 取得窗口句柄
		if not self.hwnd:
			print("窗口找不到，请确认窗口句柄名称：【%s】" % wdname)
			exit()
		win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
		size = win32gui.GetWindowRect(self.hwnd)
		print("窗口位置：", size)

	@staticmethod
	def tuisong(cishu, text):
		api = "https://sc.ftqq.com/SCU50613T4fd24ba6562a59064776ec0f9ed1edb75ccd7a156a8ec.send"
		title = "当前已运行" + str(cishu) + "次" + "，" + text
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
		time.sleep(0.1)
		pyg.mouseDown()
		pyg.mouseUp()

	def start(self):  # 程序入口、控制中心
		global tuisong_time
		cf = configparser.ConfigParser()
		cf.read("config.ini")  # 读取配置文件
		count = int(cf.get("config", "count"))
		filename = "config.ini"  # 监控配置文件改动
		info = os.stat(filename)
		size = win32gui.GetWindowRect(self.hwnd)
		topx, topy = size[0], size[1]
		while True:
			time.sleep(0.5)
			self.dianji(topx + 10, topy + 860)
			jd = pyg.locateOnScreen('JueDou.png', confidence=0.60, grayscale=True)
			hao = pyg.locateOnScreen('Hao.png', confidence=0.80, grayscale=True)
			cd = pyg.locateOnScreen('CaiDan.png', confidence=0.80, grayscale=True)
			xyb = pyg.locateOnScreen('XiaYiBu.png', confidence=0.80, grayscale=True)
			qr = pyg.locateOnScreen('QueRen.png', confidence=0.80, grayscale=True)
			cs = pyg.locateOnScreen('Chongshi.png', confidence=0.80, grayscale=True)

			if cs is not None:
				poscs = cs
				s_x, s_y = pyg.center(poscs)
				self.dianji(s_x, s_y)  # 点击重试
				logger.info('无网络>重试')

			if jd is not None:
				posjd = jd
				s_x, s_y = pyg.center(posjd)
				time.sleep(1)
				self.dianji(s_x, s_y)  # 点击决斗
				time.sleep(0.5)
				self.dianji(s_x, s_y)  # 点击决斗
				count = count + 1
				cf.set('config', 'count', str(count))
				cf.write(open("config.ini", 'w'))  # 写入count次数
				filename = "config.ini"  # 监控配置文件改动
				info = os.stat(filename)
				logger.info('决斗！已对战%s次', str(count))
				while True:
					time.sleep(0.2)
					zd = pyg.locateOnScreen('zhongduan.png', confidence=0.80, grayscale=True)
					if zd is not None:
						while True:
							time.sleep(0.5)
							self.dianji(topx + 10, topy + 860)
							drw = pyg.locateOnScreen('duorenwu.png', confidence=0.80, grayscale=True)
							if drw is not None:
								break
						break
				pyg.press('f2')  # 点击多任务键
				time.sleep(32)
				pyg.press('f2')  # 点击多任务键

			if cd is not None:
				poscd = cd
				s_x, s_y = pyg.center(poscd)
				self.dianji(s_x, s_y)  # 点击菜单
				logger.info('菜单')
				pyg.press('f2')  # 点击多任务键
				time.sleep(32)
				pyg.press('f2')  # 点击多任务键

			js = pyg.locateOnScreen('Jieshu.png', confidence=0.80, grayscale=True)
			if js is not None:
				posjs = js
				s_x, s_y = pyg.center(posjs)
				self.dianji(s_x, s_y)  # 点击结束回合
				logger.info('结束回合')
			if qr is not None:
				self.dianji(topx + 100, topy + 670)
				time.sleep(0.2)
				self.dianji(topx + 300, topy + 670)
				time.sleep(0.2)
				self.dianji(topx + 270, topy + 837)  # 点击确认
				logger.info('确认')
			if hao is not None:
				poshao = hao
				s_x, s_y = pyg.center(poshao)
				self.dianji(s_x, s_y)  # 点击好
				logger.info('好')
			if xyb is not None:
				posxyb = xyb
				s_x, s_y = pyg.center(posxyb)
				self.dianji(s_x, s_y)  # 点击下一步
				logger.info('下一步')
			if int(str(time.localtime().tm_min)[-1]) is 0:  # 每10分钟检测一次
				if time.time() - info.st_mtime > 600:  # 文件没有改动超过10分钟微信推送提醒
					if tuisong_time is None or time.time() - tuisong_time > 600:
						self.tuisong(count, "脚本出毛病了！")
						tuisong_time = time.time()
				if int(str(time.localtime().tm_min)) == 00:
					if time.time() - info.st_mtime < 600:
						if tuisong_time is None or time.time() - tuisong_time > 600:
							self.tuisong(count, "脚本正常运行！")
							tuisong_time = time.time()


if __name__ == "__main__":
	# WindowsName = u'Yu-Gi-Oh! DUEL LINKS'
	WindowsName = u'雷电模拟器'
	# WindowsName = u'BlueStacks App Player'
	demo = GameAssist(WindowsName)
	demo.start()
