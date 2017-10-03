"""
xjhorse项目Django配置

由'django-admin startproject'生成（Django版本为1.10.6）

关于此配置文件的细节请参阅：
https://docs.djangoproject.com/en/1.10/topics/settings/

可配置的参数列表及其具体取值请参阅：
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_d*=$^f+c2)t@_7h9f4p(u%ijkq@_2aqy=8w=8+&8zkxy&ld-%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.xjhorse.net']

# Application definition
AUTHENTICATION_BACKENDS = (

    # 尽管有了allauth，Django admin仍然需要以下认证模块来完成通过用户名登录
    'django.contrib.auth.backends.ModelBackend',

    # allauth特定的认证方法，如通过e-mail登录
    'allauth.account.auth_backends.AuthenticationBackend',
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 便于使用bootstrap forms
    'bootstrap3',

    #  allauth在django需要以下配置
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.baidu',     # 1、百度
    'allauth.socialaccount.providers.taobao',    # 2、淘宝
    'allauth.socialaccount.providers.qq',        # 3、QQ
    'allauth.socialaccount.providers.weixin',    # 4、微信
    'allauth.socialaccount.providers.google',    # 5、谷歌
    'allauth.socialaccount.providers.facebook',  # 6、脸谱
    'allauth.socialaccount.providers.github',    # 7、github



     # 新疆马业首页
    'homePage',
    # 用户个人资料，目前主要为了让用户能够选择自己偏好的语言
    'userProfile',

    'oauth2_provider',       # 授权服务提供者
    'corsheaders',           # 跨域授权
    'rest_framework',        # RESTful WebService, Django轻量级Web服务框架
]

# 指定 Django轻量级Web服务框架使用新的后台认证服务
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope'}
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',                        # 跨域授权
]

ROOT_URLCONF = 'xjhorse.urls'
CORS_ORIGIN_ALLOW_ALL = True                                        # 跨域授权（允许来自所有域的请求）
X_FRAME_OPTIONS = 'DENY'                                            # 点击劫持保护
CSRF_COOKIE_HTTPONLY = True                                         # 防止恶意JavaScript绕过CSRF保护
SECURE_CONTENT_TYPE_NOSNIFF = True                                  # 禁止浏览器尝试猜测内容的类型
SECURE_BROWSER_XSS_FILTER = True                                    # 跨站脚本保护
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')       # 使用https协议
# SECURE_HSTS_SECONDS = 3600
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# allauth在django需要以下配置
SITE_ID = 1
# 登录成功后重定向URL
LOGIN_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'  # 使用用户名或邮箱登陆
ACCOUNT_USERNAME_REQUIRED = True                  # 必须提供用户名
ACCOUNT_EMAIL_REQUIRED = True                     # 必须提供邮箱
ACCOUNT_USERNAME_MIN_LENGTH = 3                   # 用户名最少由3个字符组成
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'          # 强制Email验证，未通过Email验证用户无法登陆
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"    # 用户名数据库字段名称
SOCIALACCOUNT_AUTO_SIGNUP = False                 # 禁止社交账号自动登录

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email'],
        'METHOD': 'oauth2'
    },
    'google':
        { 'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': { 'access_type': 'online' }
    },
}


CRISPY_TEMPLATE_PACK = "bootstrap3"

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'                       # SMTP地址
EMAIL_PORT = 25                                  # SMTP端口
EMAIL_HOST_USER = 'ztaihong@qq.com'              # QQ的邮箱
EMAIL_HOST_PASSWORD = 'fdfpeslrpywygjfh'         # QQ SMTP验证码
EMAIL_SUBJECT_PREFIX = u'新疆马业'                # 为邮件标题前缀
EMAIL_USE_TLS = True                             # 与SMTP服务器通信时，是否启动TLS链接(安全链接)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER             # 发件人邮箱

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates'), ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # needed for admin templates
                'django.contrib.auth.context_processors.auth',
                # these *may* not be needed
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # allauth needs this from django
                'django.template.context_processors.request',
            ],
        }
    },
]

WSGI_APPLICATION = 'xjhorse.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 网站语言（国际化）
# https://docs.djangoproject.com/en/1.10/topics/i18n/
from django.conf import global_settings
gettext_noop = lambda s: s

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
  ('en-us', 'English'),
  ('zh-hans', '简体中文'),
  ('ug-ar', 'ئۇيغۇر تىلى'),
  ('kk-ar', 'قازاق ٴتىلى‎'),
)

EXTRA_LANG_INFO = {
    'ug-ar': {
        'bidi': True,     # 从右到左
        'code': 'ug-ar',
        'name': 'Uyghur',
        'name_local': u'\u0626\u06C7\u064A\u063A\u06C7\u0631 \u062A\u0649\u0644\u0649', #unicode编码
    },
    'kk-ar': {
        'bidi': True,     # 从右到左
        'code': 'kk-ar',
        'name': 'Kazakh',
        'name_local': u'\u0642\u0627\u0632\u0627\u0642\u0634\u0627',# unicode编码
    },
}
# 添加Django未提供的自定义语言
import django.conf.locale
laninfo = django.conf.locale.LANG_INFO
laninfo.update(EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = laninfo

# 使用BiDi (从右到左) 布局的语言
LANGUAGES_BIDI = global_settings.LANGUAGES_BIDI +  ["kk-ar", "ug-ar",]



TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 静态文件 (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# 告诉Django除了在每个app中寻找静态文件之外，还可以在项目根目录的static目录中寻找静态文件
# 独立于具体app的共用静态文件夹，位于项目根目录
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# 当运行python manage.py collectstatic时，Django会把所有静态文件收集到项目根目录的staticfiles目录中
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
