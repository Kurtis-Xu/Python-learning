# 1. 找到未加密的参数
# 2. 想办法将参数加密（按照网易的逻辑），params，encSecKey
# 3. 请求到网易，拿到评论信息
import base64
import json

import requests
from Crypto.Cipher import AES

"""
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131), d = new RSAKeyPair(b,"",c), e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d), f
    }
"""

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

data = dict(
    csrf_token='', cursor='-1', offset='0', orderType='1', pageNo='1', pageSize='20', rid='R_SO_4_1325905146',
    threadId='R_SO_4_1325905146'
)

magic_a = 'DjxqQJqz4TOPWS3v'
magic_e = '010001'
magic_f = (
    '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf'
    '695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b'
    '8e289dc6935b3ece0462db0a22b8e7'
)
magic_g = '0CoJUm6Qyw8W8jud'

iv = '0102030405060708'

enc_key = (
    'dabf557acb403846bdf114d828cfc70fe0e4ba9fcac119f4d21b0feb0d0ca7efd39bf4f160d56267099b0e53d842af635f44ff8d2a14818a73'
    'bf0906021b1c222241ef05a334060956eed604c9b395b8179142639f4f6d93c6d1568a5c35444677624b42e4f30fce0d45c78005b818447839'
    '4ccc0eb18c19db81b21af95fece4'
)

def to_16(dat):
    pad = 16 - len(dat) % 16
    dat += chr(pad) * pad
    return dat

def get_params(dat: str):
    base = enc_params(dat, magic_g)
    return enc_params(base, magic_a)

def enc_params(dat, key):
    aes = AES.new(key=key.encode('utf-8'), IV=iv.encode('utf-8'), mode=AES.MODE_CBC)
    dat = to_16(dat)
    bs = aes.encrypt(dat.encode('utf-8'))
    return str(base64.b64encode(bs), 'utf-8')

res = requests.post(url, data=dict(params=get_params(json.dumps(data)), encSecKey=enc_key))

print(res.text)
