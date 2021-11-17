import requests
class TestFirst:
        def test_get(self):
            r=requests.get("https://httpbin.testing-studio.com/get")
            print(r.json())
            print(r.text)
            assert r.status_code==200

        def test_query(self):
            payloads = {
                'user': 'xiaoming',
                'password': 123,
                "age": 18
            }
            url = "https://httpbin.testing-studio.com/get"
            r=requests.get(url=url,params=payloads)
            print(r.text)
            assert r.status_code==200

        def test_form(self):
            payloads={
                'user':'xiaoming',
                'password':123,
                "age":18
            }
            url="https://httpbin.testing-studio.com/post"
            r=requests.post(url=url,data=payloads)
            print(r.text)
            assert r.status_code==200
            assert r.json()['form']['age']=='18'

        def test_file(self):
            files={'file':open('report.xls','rb')}
            url="https://httpbin.testing-studio.com/post"
            r=requests.post(url=url,files=files)
            print(r.text)
            assert r.status_code==200

        def test_getheaders(self):
            headers={
                'User-Agent':'my-app/0.0.1'
            }
            url="https://httpbin.testing-studio.com/get"
            r=requests.get(url=url,headers=headers)
            print(r.text)
            assert  r.json()['headers']['Host']=="httpbin.testing-studio.com"

        def test_getcookies(self):
            cookies=dict(cookie_a='abc')
            url="https://httpbin.testing-studio.com/get"
            r=requests.get(url=url,cookies=cookies)
            print(r.json())
            print(r.text)
            assert r.json()['headers']['Cookie']=='cookie_a=abc'