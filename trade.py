# -*- coding: utf-8 -*-

import requests
import time
import login

class trade(object):

	def __init__(self, account):
		self.account = account
		
	def get_trade_list(self, since, coin, type):
		params = self.account.get_trade_list_params(since, coin, type)
		url = 'https://www.jubi.com/api/v1/trade_list/'
		self.list = requests.post(url = url, data = params).json()
		return self.list

	def get_trade_view(self, id, coin):
		params = self.account.get_trade_view_params(id, coin)
		url = 'https://www.jubi.com/api/v1/trade_view/'
		self.view = requests.post(url = url, data = params).json()
		return self.view

	def trade_cancel(self, id, coin):
		params = self.account.get_trade_view_params(id, coin)
		url = 'https://www.jubi.com/api/v1/trade_cancel/'
		self.cancel = requests.post(url = url, data = params).json()
		return self.cancel
	
	def trade_add(self, amount, price, type, coin):
		params = self.account.get_trade_add_params(amount, price, type, coin)
		#print params
		url = 'https://www.jubi.com/api/v1/trade_add/'
		self.add = requests.post(url = url, data = params).json()
		#print self.add
		return self.add
