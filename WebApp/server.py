def render_template(template_name, context = {}):

    with open(template_name, 'r') as file:
        html = file.read()
        html = html.format(**context)

    return html


def app(environ, start_response):

    path = environ.get("PATH_INFO")

    if path.endswith("/"):
        path = path[:-1]

    if path == "":
        data = render_template('index.html')
    elif path == "/contact":
        data = render_template('contact.html')
    else:
        data = render_template(template_name='404.html', context={"path": path})

    data = data.encode("utf-8")

    start_response("200 OK", [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(data)))
    ])

    return iter([data])

