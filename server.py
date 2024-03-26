from bottle import route, run, request


@route("/")
def root():
    return "latest/"

@route("/2024-03-26")
@route("/2024-03-26/")
@route("/latest/")
@route("/latest")
def metadata():
    return 'stat\n'

@route("/2024-03-26/stat")
@route("/latest/stat")
def connection_status():
    """return Client IP Address"""

    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get("REMOTE_ADDR")
    return ['Your IP is: {}\n'.format(client_ip)]


run(host='0.0.0.0', port='8080', debug=True)
