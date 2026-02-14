def parse_header(value):
    """Minimal shim of cgi.parse_header used by httpx.Response.charset_encoding.

    Returns (main_value, params_dict).
    This handles typical Content-Type headers like:
        'text/html; charset=utf-8'
    """
    if not value:
        return "", {}
    parts = [p.strip() for p in value.split(";")]
    main = parts[0].lower()
    params = {}
    for param in parts[1:]:
        if "=" in param:
            k, v = param.split("=", 1)
            k = k.strip().lower()
            v = v.strip().strip('"').strip("'")
            params[k] = v
    return main, params
