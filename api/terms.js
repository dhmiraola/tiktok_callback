def handler(request, response):
    html = """
    <html>
      <head><title>Privacy Policy</title></head>
      <body style="font-family:sans-serif; padding:20px;">
        <h1>Privacy Policy</h1>
        <p>This app does not collect, store or process any personal user information.</p>
        <p>All data used is for demonstration and testing of the TikTok API.</p>
      </body>
    </html>
    """
    response.status_code = 200
    response.headers["Content-Type"] = "text/html"
    response.body = html
    return response
