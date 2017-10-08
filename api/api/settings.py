import environ
from django.utils.translation import ugettext_lazy as _

root = environ.Path(__file__) - 2

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, '^+!+nuu710@$)vnqdilsg&2q471#n7szcxxv8-=&xp!c+bau#-'),
    STATIC_URL=(str, '/static/'),
    MEDIA_URL=(str, '/media/'),
    DATABASE_URL=(str, 'psql://postgres:postgres@localhost:5432/backend'),
    ALLOWED_HOSTS=(list, ['127.0.0.1']),
    ADMIN_EMAIL=(str, ''),
)

BASE_DIR = root()
public_root = root.path('public/')
ADMINS = (
    ('Admin backend', env('ADMIN_EMAIL')),
)
MANAGERS = ADMINS

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'cube',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [public_root('templates')],
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

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': env.db('DATABASE_URL')
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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-es'

LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (public_root('locale'),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_DIRS = (public_root('static'),)
STATIC_ROOT = public_root('staticfiles')
STATIC_URL = env('STATIC_URL')
MEDIA_ROOT = public_root('media')
MEDIA_URL = env('MEDIA_URL')

# Config DRF
REST_FRAMEWORK = {}

LOGIN_URL = '/admin/login/'
LOGOUT_URL = '/admin/logout/'
