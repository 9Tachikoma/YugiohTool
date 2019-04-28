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
import sys
import win32gui
import time
import pyautogui as pyg
import configparser
import logging

importlib.reload(sys)


class GameAssist:
	def __init__(self, wdname):  # 初始化
		self.hwnd = win32gui.FindWindow(0, wdname)  # 取得窗口句柄
		if not self.hwnd:
			print("窗口找不到，请确认窗口句柄名称：【%s】" % wdname)
			exit()
		win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
		size = win32gui.GetWindowRect(self.hwnd)
		print("窗口位置：", size)

	def start(self):  # 程序入口、控制中心
		cf = configparser.ConfigParser()
		cf.read("config.ini")  # 读取配置文件
		count = int(cf.get("config", "count"))
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
		size = win32gui.GetWindowRect(self.hwnd)
		topx, topy = size[0], size[1]
		while True:
			time.sleep(0.5)
			pyg.click(topx + 10, topy + 860)
			jd = pyg.locateOnScreen('JueDou.png', confidence=0.60, grayscale=True)
			hao = pyg.locateOnScreen('Hao.png', confidence=0.80, grayscale=True)
			cd = pyg.locateOnScreen('CaiDan.png', confidence=0.80, grayscale=True)
			xyb = pyg.locateOnScreen('XiaYiBu.png', confidence=0.80, grayscale=True)
			qr = pyg.locateOnScreen('QueRen.png', confidence=0.80, grayscale=True)
			if jd is not None:
				posjd = jd
				s_x, s_y = pyg.center(posjd)
				pyg.click(s_x, s_y)  # 点击决斗
				count = count + 1
				cf.set('config', 'count', str(count))
				cf.write(open("config.ini", 'w'))  # 写入count次数
				time.sleep(0.5)
				logger.info('决斗！已对战%s次', str(count))
			if cd is not None:
				poscd = cd
				s_x, s_y = pyg.center(poscd)
				pyg.click(s_x, s_y)  # 点击菜单
				logger.info('菜单')
				while True:
					time.sleep(0.5)
					js = pyg.locateOnScreen('Jieshu.png', confidence=0.80, grayscale=True)
					if js is not None:
						posjs = js
						s_x, s_y = pyg.center(posjs)
						pyg.click(s_x, s_y)  # 点击结束回合
						logger.info('结束回合')
						break
			if qr is not None:
				pyg.click(topx + 100, topy + 670)
				time.sleep(0.2)
				pyg.click(topx + 300, topy + 670)
				time.sleep(0.2)
				pyg.click(topx + 270, topy + 837)  # 点击确认
				logger.info('确认')
			if hao is not None:
				poshao = hao
				s_x, s_y = pyg.center(poshao)
				pyg.click(s_x, s_y)  # 点击好
				logger.info('好')
			if xyb is not None:
				posxyb = xyb
				s_x, s_y = pyg.center(posxyb)
				pyg.click(s_x, s_y)  # 点击下一步
				logger.info('下一步')


if __name__ == "__main__":
	WindowsName = u'夜神模拟器'
	demo = GameAssist(WindowsName)
	demo.start()
