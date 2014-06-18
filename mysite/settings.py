"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mdwgzsb6b&xn5zypil*54gynztyp7r7a(3j_b)&7wvv&6by&hx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

TEMPLATE_DEBUG = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
        os.path.join(os.path.dirname(__file__), 'templates/').replace('\\','/'),
        os.path.join(os.path.dirname(__file__), 'templatetags/').replace('\\','/'),
        
    )

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',    
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    # 'UserSetup',
    # 'AuthTool',
    
    'Discussion',
    'KFLProduct',
    'Tutorial',

    # 'ResultUpdater',
    # 'LockManagement',
    # 'BonuSimulation',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'mysite.middleware.SessionExpiredMiddleware'
)





ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    
)

FILE_UPLOAD_HANDLERS = ("django.core.files.uploadhandler.MemoryFileUploadHandler",
                        "django.core.files.uploadhandler.TemporaryFileUploadHandler",)



MEDIA_ROOT = os.path.join(BASE_DIR, "mysite/MEDIA")
MEDIA_URL = '/MEDIA/'
    
#     )


