import requests
import fake_headers
headers = fake_headers.Headers(headers=False).generate()

s = requests.session()
requests.utils.add_dict_to_cookiejar(s.cookies,{'hha':'666'})

s.cookies.update({'xixi':'66'})

s.cookies = requests.utils.cookiejar_from_dict({'fugai':'le'})

requests.utils.add_dict_to_cookiejar(s.cookies,{'anthor':'huohuo'})

cookie_obj = requests.cookies.create_cookie(domain = 'httpbin.org',name= 'baidu',value = 'cookie')
s.cookies.set_cookie(cookie_obj)

# s.cookies.set()
resp = s.get('https://httpbin.org/get',headers=headers)
if resp.status_code ==  200:
    
    print(resp.text)
   