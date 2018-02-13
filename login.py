# -*- coding: utf-8 -*-

"""
成功请求的参数顺序：
signature,nonce,key
nonce,		,key
(nonce参数一定要在key前面)
"""

import requests
import time
import hashlib
import hmac
import collections
import urllib
import urllib2

class Jubi(object):

	def __init__(self, public_key, private_key):
		self.public_key = public_key
		self.private_key = private_key

	def get_nonce(self):
		curr_stamp = time.time()*100
		nonce = int(curr_stamp)
		return nonce

	def get_md5(self,s):
		m = hashlib.md5()
		m.update(s.encode())
		return m.hexdigest()

	def get_params(self):
		nonce_value = self.get_nonce()
		key_value = self.public_key
		private_key = self.private_key
		string = ('nonce=' + str(nonce_value) + '&' + 'key=' + key_value).encode('utf-8')
		private_key_md5 = self.get_md5(private_key).encode('utf-8')
		signature = hmac.new(private_key_md5, string, digestmod=hashlib.sha256).hexdigest()
		dict_ordered = collections.OrderedDict()
		dict_ordered['signature'] = signature
		dict_ordered['nonce'] = nonce_value
		dict_ordered['key'] = key_value
		return dict_ordered
		
	def get_trade_list_params(self, since, coin, type):
		nonce_value = self.get_nonce()
		key_value = self.public_key
		private_key = self.private_key
		string = ('nonce=' + str(nonce_value) + '&' + 'key=' + key_value + '&since=' + str(since) + '&coin=' + coin + '&type=' +type).encode('utf-8')
		private_key_md5 = self.get_md5(private_key).encode('utf-8')
		signature = hmac.new(private_key_md5, string, digestmod=hashlib.sha256).hexdigest()
		dict_ordered = collections.OrderedDict()
		dict_ordered['signature'] = signature
		dict_ordered['nonce'] = nonce_value
		dict_ordered['key'] = key_value
		dict_ordered['since'] = since
		dict_ordered['coin'] = coin
		dict_ordered['type'] = type
		return dict_ordered
		
	def get_trade_view_params(self, id, coin):
		nonce_value = self.get_nonce()
		key_value = self.public_key
		private_key = self.private_key
		string = ('nonce=' + str(nonce_value) + '&' + 'key=' + key_value + '&id=' + str(id) + '&coin=' + coin).encode('utf-8')
		private_key_md5 = self.get_md5(private_key).encode('utf-8')
		signature = hmac.new(private_key_md5, string, digestmod=hashlib.sha256).hexdigest()
		dict_ordered = collections.OrderedDict()
		dict_ordered['signature'] = signature
		dict_ordered['nonce'] = nonce_value
		dict_ordered['key'] = key_value
		dict_ordered['id'] = id
		dict_ordered['coin'] = coin
		return dict_ordered
		
	def get_trade_add_params(self, amount, price, type, coin):
		nonce_value = self.get_nonce()
		key_value = self.public_key
		private_key = self.private_key
		string = ('nonce=' + str(nonce_value) + '&key=' + key_value + '&amount=' + str(amount) +'&price=' +str(price) +'&type=' +type +'&coin='+coin).encode('utf-8')
		#string = "amount="+str(amount)+"&nonce="+str(nonce_value)+"&type="+type+"&key="+key_value+"&price="+str(price)+"&coin="+coin
		private_key_md5 = self.get_md5(private_key).encode('utf-8')
		signature = hmac.new(private_key_md5, string, digestmod=hashlib.sha256).hexdigest()
		
		dict_ordered = collections.OrderedDict()
		dict_ordered['signature'] = signature
		dict_ordered['nonce'] = nonce_value
		dict_ordered['key'] = key_value
		dict_ordered['amount'] = amount
		dict_ordered['price'] = price
		dict_ordered['type'] = type
		dict_ordered['coin'] = coin
		
		return dict_ordered
	
	'''
	def get_nonce_time(self):
		lens = 12
		curr_stamp = time.time()*100
		nonece=int(curr_stamp)
		return nonece
		
	def getHash(self,s):
		m=hashlib.md5()
		m.update(s)
		return m.hexdigest()
		
	def getAccount(self):
		url='https://www.jubi.com/api/v1/balance/'

		nonce_value=self.get_nonce_time()
		print nonce_value
		key_value=self.public_key
		private_key=self.private_key

		s='nonce='+str(nonce_value)+'&'+'key='+key_value

		print s

        #signature是签名，是将amount price type nonce key等参数通过'&'字符连接起来通过md5(私钥)为key进行sha256算法加密得到的值.
		md5=self.getHash(private_key)
		print md5
		print type(md5)

		msg=bytes(s).encode('utf-8')
		key=bytes(md5).encode('utf-8')
		signature =hmac.new(key,msg,digestmod=hashlib.sha256).digest()
		print signature
		print type(signature)
		sig = signature
		print signature
		data_wrap={'nonce':nonce_value,'key':key_value,'signature':signature}

		print data_wrap

		data_en=urllib.urlencode(data_wrap)
		req=urllib2.Request(url,data=data_en)
		resp=urllib2.urlopen(req).read()
		print resp








