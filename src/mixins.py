from starlette.requests import Request


def contact_mixin(request: Request):
    return {
        'request': request,
        'telegram': 'https://t.me/thommyserpentes',
        'email': 'mailto:bots.from.duck@gmail.com'
    }
