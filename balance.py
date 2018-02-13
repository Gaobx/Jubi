# -*- coding: utf-8 -*-

import requests
import time
import login

class balance(object):

	def __init__(self, account):
		self.account = account
		self.url = 'https://www.jubi.com/api/v1/balance/'
		self.data = self.account.get_params()
		self.resp = requests.post(url = self.url, data = self.data).json()
		
	def get_all_balances(self):
		return self.resp
		
	def get_asset(self):
		return self.resp['asset']
		
	def get_coin_balances(self, coin):
		#Coin_balance = coin + '_balance'
		#Coin_lock = coin + '_lock'
		coin_balances = {'balance' : self.get_coin_balance(coin), 'lock' : self.get_coin_lock(coin)}
		return coin_balances				
		
	def get_coin_balance(self, coin):
		Coin = coin + '_balance'
		return self.resp[Coin]
		
	def get_coin_lock(self, coin):
		Coin = coin + '_lock'
		return self.resp[Coin]
		
'''	
account = login.Jubi('3wq19-u2j4f-hvtjm-4pi1g-6ezde-nbrvk-eyh5y','Z!1q7-C,(kv-Ju36v-Fk]DQ-ea!*$-Kt*6E-{.C{b')
ban = balance(account)
all = ban.get_all_balances()
print all
ltc_balance = ban.get_coin_balance('ltc')
print ltc_balance
ltc_balances = ban.get_coin_balances('ltc')
print ltc_balances
print ltc_balances['lock']
asset = ban.get_asset()
print asset
'''