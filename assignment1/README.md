 python3 api.py
 
curl -i -X POST  -F "data=@foo.py" http://127.0.0.1:8000/api/v1/scripts/
HTTP/1.1 100 Continue

HTTP/1.0 201 CREATED
Content-Type: text/html; charset=utf-8
Content-Length: 49
Server: Werkzeug/0.12.2 Python/3.5.2
Date: Thu, 30 Nov 2017 00:25:53 GMT

{"script-id": "b312eb8f8a3148b19a74918212c0db04"}



curl -i  http://localhost:8000/api/v1/scripts/b312eb8f8a3148b19a74918212c0db04
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 13
Server: Werkzeug/0.12.2 Python/3.5.2
Date: Thu, 30 Nov 2017 00:26:06 GMT

Hello World!


