import qcloud_cos as qcloud
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

appid = config['appid'].encode('utf8')
secret_id = config['secret_id'].encode('utf8')
secret_key = config['secret_key'].encode('utf8')


def getAllFile(bucket,path):

    while True:

        listret = cos.list(bucket, path, 50)

        if listret['code'] != 0:
            print listret['message']
            return -1

        if len(listret['data']['infos']) == 0:
            return -1

        for info in listret['data']['infos']:
            name = info['name'].encode('utf8')
            fullpath = path+'/'+ name
            if info.has_key('sha'):
                print "fullpath:" + fullpath
                urllib.urlretrieve("http://img.mixiong.tv"+fullpath, "/Users/mazhiyu/Downloads/pic/"+name.split('/')[-1])
            else:
                allfile = getAllFile(bucket, fullpath)
                print "allfile:" + str(allfile)
                if allfile != 0:
                   return allfile
        return 0


cos = qcloud.Cos(appid, secret_id, secret_key)
result = getAllFile(bucket,path)
print result