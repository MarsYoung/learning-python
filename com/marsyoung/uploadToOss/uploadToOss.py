import oss2
import sys
import string
import urllib
import json
import urllib2
import requests

with open('./app_conf.json', 'rb') as f:
	config = json.load(f)

bucket='images'
path="/"

AccessKeyId = config['AccessKeyId'].encode('utf8')
AccessKeySecret = config['AccessKeySecret'].encode('utf8')
Endpoint = config['Endpoint'].encode('utf8')
Bucket = config['Bucket'].encode('utf8')


auth = oss2.Auth(AccessKeyId, AccessKeySecret)
bucket = oss2.Bucket(auth, Endpoint, Bucket)

with open('local.txt', 'rb') as fileobj:
    result = bucket.put_object('remote.txt', fileobj)

print('http status: {0}'.format(result.status))
print('request_id: {0}'.format(result.request_id))
print('ETag: {0}'.format(result.etag))
print('date: {0}'.format(result.headers['date']))