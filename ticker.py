# -*- coding: utf-8 -*-

import requests
import time
import login
import urllib2
import json

class ticker(object):

	def __init__(self, coin):
		self.url = 'https://www.jubi.com/api/v1/ticker/'
		self.coin = coin
			
	def get_coin_ticker(self):
		self.resp = requests.post(url = self.url, data = {'coin': self.coin}).json()
		response = urllib2.urlopen('https://www.jubi.com/coin/trends')
		html = response.read().decode("utf8","ignore").encode("gbk","ignore")
		trends = json.loads(html)
		
		self.resp['yprice'] = trends[self.coin]['yprice']
		
		last = self.resp['last'].encode("utf-8")	#unicode to string
		self.resp['last'] = float(last)				#string to float
		buy = self.resp['buy'].encode("utf-8")
		self.resp['buy'] = float(buy)
		sell = self.resp['sell'].encode("utf-8")
		self.resp['sell'] = float(sell)
		high = self.resp['high'].encode("utf-8")
		self.resp['high'] = float(high)
		low = self.resp['low'].encode("utf-8")
		self.resp['low'] = float(low)
		
		if self.resp['yprice'] != 0:		
			self.resp['rate'] = (self.resp['last']/self.resp['yprice']) - 1
		else:
			self.resp['rate'] = -1.0
		return self.resp
		
	def calc_all_rate(self):
		allTicker = self.get_allTicker()
		#print allTicker
		self.zero_num = 0
		headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
		
		request = urllib2.Request('https://www.jubi.com/coin/trends', headers = headers)
		response = urllib2.urlopen(request)
		#response = urllib2.urlopen('https://www.jubi.com/coin/trends')
		html = response.read().decode("utf8","ignore").encode("gbk","ignore")
		trends = json.loads(html)
		for coin in trends:
			coin_yprice = trends[coin]['yprice']
			allTicker[coin]['yprice'] = coin_yprice
			
			if coin_yprice != 0:
				allTicker[coin]['rate'] = round(allTicker[coin]['last']/coin_yprice - 1, 4)
			else:
				allTicker[coin]['rate'] = -1.0000
			if allTicker[coin]['rate'] == 0:
				self.zero_num += 1
		#print self.zero_num
			#print coin , allTicker[coin]['rate']\
		return allTicker
			
	def sort_by_rate(self):
		allTicker = self.calc_all_rate()
		#print allTicker
		#for coin in allTicker:
		#	backitems = [allTicker[coin]['rate'], coin]
		self.backitems=[[allTicker[coin]['rate'],coin] for coin in allTicker]
		self.backitems.sort(reverse = True)
		'''for i in range(0, len(backitems)):
			print backitems[i]'''
		return self.backitems
	
	def print_ticker(self):
		for i in range(0, len(self.backitems)):
			print self.backitems[i]
	
	def get_allTicker(self):
		url = 'https://www.jubi.com/api/v1/allticker/'
		result = requests.post(url = url).json()
		return result
		
	def get_orders(self):
		url = 'https://www.jubi.com/api/v1/orders/'
		result = requests.post(url = url, data = self.coin).json()
		return result
	
"""
	def get_yprice(self):
		return get_coin_ticker()['yprice']
	
	def get_rate(self):
		return get_coin_ticker()['rate']
		
	def get_high(self):
		self.resp = requests.post(url = self.url, data = self.coin).json()
		return self.resp['high']
		
	def get_low(self):
		self.resp = requests.post(url = self.url, data = self.coin).json()
		return self.resp['low']
		
	def get_buy(self):
		self.resp = requests.post(url = self.url, data = self.coin).json()
		return self.resp['buy']
		
	def get_sell(self):
		self.resp = requests.post(url = self.url, data = self.coin).json()
		return self.resp['sell']
		
	def get_last(self):
		self.resp = requests.post(url = self.url, data = self.coin).json()
		return self.resp['last']

	def get_vol(self):
		self.resp = requests.post(url = self.url, data = self.coin).json()
		return self.resp['vol']
		
	def get_volume(self):
		self.resp = requests.post(url = self.url, data = self.coin).json()
		return self.resp['vol']

	def get_depth(self):
		url = 'https://www.jubi.com/api/v1/depth/'
		result = requests.post(url = url, data = self.coin).json()
		return result
		
"""
	
'''
ltc_ticker = ticker("btc")
print ltc_ticker.get_coin_ticker()
#print ltc_ticker.get_last() + "\n\n\n"
#result = ltc_ticker.get_depth()
#print str(result) + "\n\n\n"
#print ltc_ticker.get_allTicker()
#ltc_ticker.calc_all_rate()
ltc_ticker.sort_by_rate()
ltc_ticker.print_ticker()
print ltc_ticker.zero_num
#print "\n\n\n\n"
#print ltc_ticker.get_orders()

#print ltc_ticker.get_coin_ticker()['yprice']
#print ltc_ticker.get_coin_ticker()['abc']
'''
