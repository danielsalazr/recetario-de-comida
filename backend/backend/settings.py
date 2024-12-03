import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# environ init
env = environ.Env()
environ.Env.read_env()
    
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True #env.bool('DEBUG', default=False)

DEFAULT_TIMEOUT = 5

#HANA CONF
# HANA_DB_USER = env.str('HANA_DB_USER')
# HANA_DB_PASS = env.str('HANA_DB_PASS')
# HANA_DB_PORT = env.str('HANA_DB_PORT')
# HANA_DB_ADDRESS = env.str('HANA_DB_ADDRESS')

SILKY_PYTHON_PROFILER = True

#TTF FONTS
URL_ARIAL_TTF = env.str('URL_ARIAL_TTF')

ALLOWED_HOSTS = ['*']

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# Application definition

INSTALLED_APPS = [
    #'admin_interface',
    #'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    #'corsheaders',
    # 'login',
    # 'MySQL',
    # 'picking',
    # 'reports',
    # 'SAP',
    # 'inventory.apps.InventoryConfig',
    'rest_framework',
    'recetas',
    'usuarios',
    'corsheaders',
    #'silk',
]

MIDDLEWARE = [
    # 'silk.middleware.SilkyMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'axes.middleware.AxesMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'




# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.str('NAME_DB'),
        'USER': env.str('USER_DB'),
        'PASSWORD': env.str('PASS_DB'),       
        #'HOST': 'localhost',
        'HOST': env.str('IP_DB'),
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
        'CONN_HEALTH_CHECKS':True,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        'CONN_MAX_AGE': 300,  # Number of seconds database connections should persist
    },

    # 'sesiones': {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": env.str('SESION_DB'), 
    #     "USER": env.str('SESION_USER_DB'),
    #     "PASSWORD": env.str('SESION_PASS_DB'),
    #     "HOST": env.str('SESION_IP_DB'),
    #     "PORT": "3306",
    # },
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/1',  # URL de conexión a Redis
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }

CACHE_TTL = 60 * 15

CORS_ALLOWED_ORIGINS = [
    'http://192.168.130.22:3000', 'http://127.0.0.1:3000', 'http://localhost:3000',
    'http://127.0.0.1',
    
]


CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000','http://192.168.130.22:3000'', http://127.0.0.1:3000',
]

CORS_ALLOW_CREDENTIALS = True


CORS_ALLOW_ALL_ORIGINS = True


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
# }


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'wms/logs/sqlLogs.log',
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'mysql.connector': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'pymysql': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Bogota' #'UTC'

USE_I18N = True

USE_L10N = True

# USE_TZ = True





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#statics
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    #"/var/www/static/",
]

#media
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AXES_ENABLED = True
# # AXES_USERNAME_FORM_FIELD = 'username'
# AXES_LOCKOUT_PARAMETERS = ['username',]
# AXES_FAILURE_LIMIT = 5
# AXES_LOCK_OUT_AT_FAILURE = True
# AXES_NEVER_LOCKOUT_WHITELIST = True
# #AXES_IP_WHITELIST = ['192.168.0.19','127.0.0.1','192.168.0.12',]
# AXES_IP_BLACKLIST = []

# # AXES_COOLOFF_TIME = 1
# AXES_ENABLE_ACCESS_FAILURE_LOG = True
# # AXES_RESET_ON_SUCCESS = True


# AUTHENTICATION_BACKENDS = [
#     # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
#     #'axes.backends.AxesStandaloneBackend', # para windows
#     'axes.backends.AxesBackend', # para linux

#     # Django ModelBackend is the default authentication backend.
#     'django.contrib.auth.backends.ModelBackend',
# ]

