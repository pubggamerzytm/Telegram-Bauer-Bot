def is_numeric(string):
    """ Also accepts '.' in the string. Function 'isnumeric()' doesn't """
    try:
        float(string)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(string)
        return True
    except (TypeError, ValueError):
        pass

    return False


def esc_md(text):
    import re

    rep = {"_": "\\_", "*": "\\*", "[": "\\[", "`": "\\`"}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))

    return pattern.sub(lambda m: rep[re.escape(m.group(0))], text)


def build_menu(buttons, n_cols=1, header_buttons=None, footer_buttons=None):
    """ Build button-menu for Telegram """
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]

    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)

    return menu


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


def split_msg(msg, max_len=None, split_char="\n", only_one=False):
    """ Restrict message length to max characters as defined by Telegram """
    if not max_len:
        import bauer.constants as con
        max_len = con.MAX_TG_MSG_LEN

    if only_one:
        return [msg[:max_len][:msg[:max_len].rfind(split_char)]]

    remaining = msg
    messages = list()
    while len(remaining) > max_len:
        split_at = remaining[:max_len].rfind(split_char)
        message = remaining[:max_len][:split_at]
        messages.append(message)
        remaining = remaining[len(message):]
    else:
        messages.append(remaining)

    return messages


def encode_url(trxid):
    import urllib.parse as ul
    return ul.quote_plus(trxid)
