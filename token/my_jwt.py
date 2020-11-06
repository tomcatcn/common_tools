#生成一个jwt格式的token
import json
import base64
import hmac
import time

class Jwt():
    def __init__(self):
        pass

    @staticmethod
    def encode(payload=None,key=None,exp=None):
        """
        返回一个jwt格式令牌
        :param payload:私有声明，字典格式
        :param key:秘钥，字符串
        :param exp:过期时间，秒
        :return:令牌,bytes
        """
        headers = {'alg':'HS256','typ':'JWT'}
        headers = json.dumps(headers,sort_keys=True,separators=(',',':')) #转化json字符串
        headers = headers.encode() #转化二进制
        headers = base64.urlsafe_b64encode(headers).replace(b'=',b'') #转为为B64加密,等号去掉，减少传输量

        payload.update({'exp':time.time()+int(exp)}) #添加过期时间

        payload = json.dumps(payload,sort_keys=True,separators=(',',':'))#转化json字符串
        payload = payload.encode() #转化二进制
        payload = base64.urlsafe_b64encode(payload).replace(b'=',b'') #转为为B64加密
        str = headers+b'.'+payload
        key = key.encode()  # 转化二进制
        signature = hmac.new(key,str,digestmod='SHA256').digest() #256加密，返回二进制
        signature = base64.urlsafe_b64encode(signature).replace(b'=',b'') #256加密

        return headers+'.'.encode()+payload+'.'.encode()+signature

    @staticmethod
    def decode(jwt_s,key):
        """
        1.检查签名,前两项再做一次hmac，与第三部分比较,失败raise
        2.检查时间戳是否过期，过期raise
        3.返回payload明文

        :param jwt_s: token
        :return: payload明文,字典
        """
        #校验
        headers_check,payload_check,signature = jwt_s.split(b'.')
        str = headers_check + b'.'+payload_check
        key = key.encode()
        signature_check = hmac.new(key, str, digestmod='SHA256').digest()  # 256加密，返回二进制
        signature_check = base64.urlsafe_b64encode(signature_check).replace(b'=',b'') #256加密
        #检验签名
        if signature_check == signature:
            #签名正确，把payload补全
            if len(payload_check) % 4 == 1:
                payload_check += b'='
            elif len(payload_check) % 4 == 2:
                payload_check += b'=='
            elif len(payload_check) % 4 == 3:
                payload_check += b'==='       
            #转化成字典
            payload_origin = base64.urlsafe_b64decode(payload_check)
            payload_jsonstr = payload_origin.decode()
            payload_dit = json.loads(payload_jsonstr)
            time_former = payload_dit['exp']
            now_time = time.time()
            #检验时间戳
            if now_time > time_former:
                #过期
                raise ValueError('time out')
            else:
                #返回私人声明
                del payload_dit['exp']
                return payload_dit
            
            


        else:
            raise ValueError('sign wrong')






if __name__ == '__main__':
    j = Jwt()
    token = j.encode(payload={'username':'x689'},key='123456',exp=5)

    result = j.decode(token,key='123456')
    print(result)