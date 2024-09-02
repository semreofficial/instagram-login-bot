import requests

def instagram_login(username, password):
    login_url = "https://www.instagram.com/accounts/login/ajax/"
    session = requests.Session()

    # İlk istek: Instagram'ın giriş formu için gerekli bilgileri toplama
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "X-CSRFToken": "",
        "Referer": "https://www.instagram.com/accounts/login/",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # CSRF token'ı alabilmek için önce Instagram sayfasını ziyaret etmeliyiz
    session.headers.update(headers)
    session.get("https://www.instagram.com/")

    # CSRF token'ı headers içine ekleme
    csrf_token = session.cookies.get("csrftoken")
    session.headers.update({"X-CSRFToken": csrf_token})

    # Giriş yapma isteği
    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    login_response = session.post(login_url, data=payload, allow_redirects=True)
    if login_response.status_code == 200 and login_response.json().get('authenticated'):
        print(f"Giriş başarılı: {username}")
        return True
    else:
        print(f"Giriş başarısız: {username}")
        return False

# Kullanıcı listesi ile giriş deneme
user_accounts = [("username1", "password1"), ("username2", "password2")]

for account in user_accounts:
    username, password = account
    success = instagram_login(username, password)
    if success:
        print(f"{username} başarıyla giriş yaptı.")
    else:
        print(f"{username} giriş başarısız.")
