import requests
from django.conf import settings

from utils.exceptions.social_login import DebugTokenException


def access_token_test(request):
    code = request.GET.get('code')
    exchange_access_token_url = 'https://graph.facebook.com/v2.9/oauth/access_token'

    # 이전에 요청했던 URL 과 같은 값 생성(Access Token 요청시 필요)
    redirect_uri = '{}{}'.format(
        settings.SITE_URL,
        request.path,
    )

    # # Access Token 을 교환할 URL
    # exchange_access_token_url = 'https://graph.facebook.com/v2.9/oauth/access_token'

    # Access Token 요청시 필요한 파라미터
    exchange_access_token_url_params = {
        'client_id': settings.FACEBOOK_APP_ID,
        'redirect_uri': redirect_uri,
        'client_secret': settings.FACEBOOK_SECRET_CODE,
        'code': code,
    }
    print(exchange_access_token_url_params)

    # Access Token 을 요청한다.
    response = requests.get(
        exchange_access_token_url,
        params=exchange_access_token_url_params,
    )
    result = response.json()
    print(result)

    # 응답받은 결과값에 'access_token'이라는 key 가 존재하면,
    if 'access_token' in result:
        # access_token key 의 value 를 반환한다.
        return result['access_token']
    elif 'error' in result:
        raise Exception(result)
    else:
        raise Exception('Unknown error')

##
# 액세스 토큰이 올바른지 검사
##
def debug_token(token):
    app_access_token = '{}|{}'.format(
        settings.FACEBOOK_APP_ID,
        settings.FACEBOOK_SECRET_CODE,
    )

    debug_token_url = 'https://graph.facebook.com/debug_token'
    debug_token_url_params = {
        'input_token': token,
        'access_token': app_access_token
    }

    response = requests.get(debug_token_url, debug_token_url_params)
    result = response.json()

    if 'error' in result['data']:
        raise DebugTokenException(result)
    else:
        return result