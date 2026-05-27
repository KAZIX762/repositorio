from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello World Python</title>
            <style>
                body {
                    font-family: Arial;
                    text-align: center;
                    padding: 50px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                }
                h1 {
                    font-size: 4em;
                }
            </style>
        </head>
        <body>
            <h1>🐍 Hello World from Python! 🌍</h1>
            <p>Esta página foi gerada por um servidor HTTP Python puro!</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

print("Servidor rodando em http://localhost:8000")
HTTPServer(('localhost', 8000), Handler).serve_forever()