"""
Django settings for controller project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import redis

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WORKLOAD_METRICS_DIR = os.path.join('/opt', 'crystal', 'workload_metrics')
NATIVE_FILTERS_DIR = os.path.join('/opt', 'crystal', 'native_filters')
STORLET_FILTERS_DIR = os.path.join('/opt', 'crystal', 'storlet_filters')
DEPENDENCY_DIR = os.path.join('/opt', 'crystal', 'dependencies')
ANALYZERS_DIR = os.path.join('/opt', 'crystal', 'job_analyzers')
JOBS_DIR = os.path.join('/opt', 'crystal', 'jobs')
CONTROLLERS_DIR = os.path.join('/opt', 'crystal', 'controllers')


NATIVE_FILTER_KEYS = ('id', 'filter_name', 'filter_type', 'language', 'dependencies', 'main', 'is_pre_put', 'is_post_put',
                      'is_pre_get', 'is_post_get', 'has_reverse', 'execution_server', 'execution_server_reverse', 'path')
STORLET_FILTER_KEYS = ('id', 'filter_name', 'filter_type', 'language', 'interface_version', 'dependencies', 'main', 'is_pre_put', 'is_post_put',
                       'is_pre_get', 'is_post_get', 'has_reverse', 'execution_server', 'execution_server_reverse', 'path')
DEPENDENCY_KEYS = ('id', 'name', 'version', 'permissions', 'path')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&yx_=2@s(evyq=l9t2efrgmgryz^ea85$csdb_rprvc-9b&#r8'  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['controller', ]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'rest_framework',
    'filters',
    'swift',
    'controller'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'api.middleware.CrystalMiddleware',
)

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Simple sqlite3 database to avoid errors pop up during testing initialization
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase.sqlite3',
    }
}

# Logging
LOGGING = {
    'version': 1,
    'formatters': {
        'standard_django': {
            '()': 'api.common_utils.LoggingColorsDjango',
            'format': '[%(asctime)s]"%(levelname)s" %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
        'standard_crystal': {
            '()': 'api.common_utils.LoggingColorsCrystal',
            'format': '[%(asctime)s]"%(levelname)s" %(name)s: %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
    'handlers': {
        'console_django': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard_django',
        },
        'console_crystal': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard_crystal',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console_django'],
            'level': 'INFO',
            'propagate': False
        },
        '': {
            'handlers': ['console_crystal'],
            'level': 'INFO',
            'propagate': False
        }
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'CET'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

# Keystone
KEYSTONE_ADMIN_URL = 'http://localhost:35357/v3'
KEYSTONE_URL = 'http://localhost:5000/v3'

# Swift
SWIFT_URL = 'http://localhost:8080/'
SWIFT_API_VERSION = 'v1'

# Redis
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DATABASE = 0
REDIS_CON_POOL = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DATABASE)

# Storlet docker image
STORLET_DOCKER_IMAGE = '192.168.2.1:5001/ubuntu_16.04_jre8_storlets'

# Openstack Admin
MANAGEMENT_ACCOUNT = 'management'
MANAGEMENT_ADMIN_USERNAME = 'manager'
MANAGEMENT_ADMIN_PASSWORD = 'manager'  # noqa

# pyactor
PYACTOR_TRANSPORT = 'http'
PYACTOR_IP = '127.0.0.1'
PYACTOR_PORT = 6899
PYACTOR_URL = PYACTOR_TRANSPORT + '://' + PYACTOR_IP + ':' + str(PYACTOR_PORT)


# Generic Consumer Actor
CONSUMER_MODULE = 'api.actors.consumer/Consumer'

# Swift Metric Actor
METRIC_MODULE = 'metrics.actors.swift_metric/SwiftMetric'

# Rule Actor
RULE_MODULE = 'policies.actors.rule/Rule'

# Transient Rule Actor
RULE_TRANSIENT_MODULE = 'policies.actors.rule_transient/TransientRule'

# Global controllers
GLOBAL_CONTROLLERS_BASE_MODULE = 'controller.dynamic_policies.rules'
METRICS_BASE_MODULE = 'controller.dynamic_policies.metrics'

# RabbitMQ
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USERNAME = 'guest'
RABBITMQ_PASSWORD = 'guest'
RABBITMQ_EXCHANGE = 'amq.topic'

# Logstash
LOGSTASH_HOST = 'localhost'
LOGSTASH_PORT = 5400

# Job analyzer executor
JOB_ANALYZER_EXECUTOR_LOCATION = '/opt/crystal/jobs/'
JOB_ANALYZER_JAVAC_PATH = '/usr/bin/javac'
JOB_ANALYZER_SPARK_FOLDER = '/usr/local/spark/'
JOB_ANALYZER_SPARK_LIBS_LOCATION = JOB_ANALYZER_SPARK_FOLDER + 'jars/'
JOB_ANALYZER_LAMBDA_PUSHDOWN_FILTER = 'lambdapushdown-1.0.jar'
JOB_ANALYZER_SPARK_MASTER_URL = 'spark://127.0.0.1:7077'
JOB_ANALYZER_AVAILABLE_RAM = '1G'
JOB_ANALYZER_AVAILABLE_CPUS = '2'
JOB_ANALYZER_CLUSTER_MODE = False
JOB_ANALYZER_HDFS_LOCATION = '/usr/local/hadoop/bin/hdfs dfs '
JOB_ANALYZER_HDFS_IP_PORT = '127.0.0.1:9000'
