#!/usr/bin/python
# coding:utf-8

"""
@author: zyatom
@contact: 70906346@qq.com
@software: PyCharm
@file: YugiohTool.py
@time: 2020/4/21 20:50
"""
import importlib
import msvcrt
import os
import sys
import time
import win32gui
import threading
import inspect
import ctypes
import configparser

import requests

from YugiohToolSteam import Steam

from YugiohToolMoniqi import Moniqi

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


def tuisong(cishu, text, serviceapi):  # 推送到手机
	api = serviceapi
	title = "脚本运行" + str(cishu) + "次" + "，" + text
	content = text
	data = {
		"text": title,
		"desp": content
	}
	requests.post(api, data=data)


tuisong_time = None


def tuisongfunction():
	global tuisong_time
	cf = configparser.ConfigParser()
	cf.read("config.ini")  # 读取配置文件
	count = int(cf.get("config", "count"))
	start_count = count
	start_time = time.time()
	serviceapi = cf.get("config", "serviceapi")
	filename = "config.ini"  # 监控配置文件改动
	while True:
		time.sleep(10)
		cf.read("config.ini")  # 读取配置文件
		info = os.stat(filename)
		count = int(cf.get("config", "count"))
		if int(str(time.localtime().tm_min)[-1]) is 0:
			# 文件没有改动超过10分钟且运行时间超过10分钟微信推送提醒
			if time.time() - info.st_mtime > 600 and time.time() - start_time > 600:
				if tuisong_time is None or time.time() - tuisong_time > 600:
					count_per_hour = count - start_count
					tuisong(count_per_hour, "脚本异常停止！", serviceapi)
					tuisong_time = time.time()
					break
			# 整点发送推送
			if int(str(time.localtime().tm_min)) == 00:
				if time.time() - info.st_mtime < 600:
					if tuisong_time is None or time.time() - tuisong_time > 600:
						count_per_hour = count - start_count
						start_count = count
						tuisong(count_per_hour, "一切正常！", serviceapi)
						tuisong_time = time.time()
		if time.time() - start_time > 1800:
			print("试用时间已到，请购买完整版或重启继续试用（按任意键退出...）")
			while True:
				pressedkey = msvcrt.getch()
				if pressedkey is not None:
					stop_thread(t_main)
					exit()


def main():
	steam = u'Yu-Gi-Oh! DUEL LINKS'  # steam
	moniqi = u'雷电模拟器'  # 模拟器
	hwnd_steam = win32gui.FindWindow(0, steam)  # 取得窗口句柄
	hwnd_moniqi = win32gui.FindWindow(0, moniqi)  # 取得窗口句柄
	if hwnd_steam:
		while True:
			print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ １、ｐｖｐＫＣ杯自杀　　　　　　　　　　　　　　　　　　　　")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ ２、ｐｖｐ排名决斗自杀　　　　　　　　　　　　　　　　　　　")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ ３、ｐｖｐ休闲决斗自杀　　　　　　　　　　　　　　　　　　　")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ ４、自动十级门　　　　　　　　　　　　　　　　　　　　　　　")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ ５、ｐｖｐ休闲决斗战斗　　　　　　　　　　　　　　　　　　　")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ ６、ｐｖｐ排名决斗战斗　　　　　　　　　　　　　　　　　　　")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
			print("┃ ７、活动组队决斗全自动（已过期） 　　　　　　　　　　　　 　")
			print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
			print("◎◎◎◎◎请输入要选择的功能前面的数字并回车◎◎◎◎◎")
			input1 = str(input(""))
			if input1 == '1' or input1 == '2' or input1 == '3':
				demo = Steam(steam, "2")
				demo.pvp_tolose_steam(input1)
			elif input1 == '4':
				demo = Steam(steam, "2")
				demo.chuansongmen_steam()
			elif input1 == '5':
				demo = Steam(steam, "2")
				demo.pvp_xiuxian_towin_steam()
			elif input1 == '6':
				demo = Steam(steam, "2")
				demo.pvp_paimin_towin_steam()
			elif input1 == '7':
				demo = Steam(steam, "2")
				demo.huodong_zuidui_steam()
			else:
				print("!!!!!输入有误,请重新输入!!!!!")
				time.sleep(1)
	elif hwnd_moniqi:
		while True:
			print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ")
			print("┃ １、ｐｖｐＫＣ杯自杀　　　　　　　　　　　　　　　　　　　　┃")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ")
			print("┃ ２、ｐｖｐ排名决斗自杀　　　　　　　　　　　　　　　　　　　┃")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ")
			print("┃ ３、ｐｖｐ休闲决斗自杀　　　　　　　　　　　　　　　　　　　┃")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ")
			print("┃ ４、自动十级门　　　　　　　　　　　　　　　　　　　　　　　┃")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ")
			print("┃ ５、ｐｖｐ休闲决斗战斗　　　　　　　　　　　　　　　　　　　┃")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ")
			print("┃ ６、ｐｖｐ排名决斗战斗　　　　　　　　　　　　　　　　　　　┃")
			print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ")
			print("┃ ７、活动组队决斗全自动（已过期） 　　　　　　　　　　　　 　┃")
			print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
			print("◎◎◎◎◎请输入要选择的功能前面的数字并回车◎◎◎◎◎")
			input1 = str(input(""))
			if input1 == '1' or input1 == '2' or input1 == '3':
				demo = Moniqi(moniqi, "2")
				demo.pvp_tolose_moniqi(input1)
			elif input1 == '4':
				demo = Moniqi(moniqi, "2")
				demo.chuansongmen_moniqi()
			elif input1 == '5':
				demo = Moniqi(moniqi, "2")
				demo.pvp_xiuxian_towin_moniqi()
			elif input1 == '6':
				demo = Moniqi(moniqi, "2")
				demo.pvp_paimin_towin_moniqi()
			elif input1 == '7':
				demo = Moniqi(moniqi, "2")
				demo.huodong_zuidui_moniqi()
			else:
				print("!!!!!输入有误,请重新输入!!!!!")
				time.sleep(1)
	else:
		print("找不到游戏王决斗链接，请打开游戏后再次尝试")
		exit()


if __name__ == '__main__':
	t_tuosong = threading.Thread(target=tuisongfunction, args=())
	t_main = threading.Thread(target=main, args=())
	t_tuosong.setDaemon(True)
	t_tuosong.start()
	t_main.start()
