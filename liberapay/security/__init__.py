from __future__ import absolute_import, division, print_function, unicode_literals


def set_default_security_headers(website, response, request=None):
    # Allow CORS for assets
    # The subdomains need this to access the assets on the main domain.
    if request is not None and request.path.raw.startswith('/assets/'):
        response.headers[b'Access-Control-Allow-Origin'] = b'*'

    # X-Frame-Options is a security measure to prevent clickjacking
    # See http://en.wikipedia.org/wiki/Clickjacking
    response.headers[b'X-Frame-Options'] = b'SAMEORIGIN'

    # CSP is a client-side protection against code injection (XSS)
    # https://scotthelme.co.uk/content-security-policy-an-introduction/
    response.headers[b'content-security-policy'] = website.csp

    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection
    response.headers[b'X-XSS-Protection'] = b'1; mode=block'

    # https://www.w3.org/TR/referrer-policy/#referrer-policy-strict-origin-when-cross-origin
    # https://caniuse.com/referrer-policy
    response.headers[b'Referrer-Policy'] = b'strict-origin-when-cross-origin'
