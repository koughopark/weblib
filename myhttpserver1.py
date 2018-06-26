from http.server import BaseHTTPRequestHandler, HTTPServer

port = 9999


# 상속받는 핸들러를 실행하라
class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # print('receive result')
        # 응답만들기
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=urf-8')
        self.end_headers()
        self.wfile.write('<h1>hahahohokorea</h1>'.encode('utf-8'))


# 서버구동
httpd = HTTPServer(('', 9999), MyHTTPRequestHandler)
# 서버주소랑 포트랑 등록한다.
print('HTTP Server Starts....')
httpd.serve_forever()  # 무한루프
