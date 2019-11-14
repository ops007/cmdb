#!/usr/bin/env python
import os
AUTH_USER_MODEL = 'users.CustomUser'

DEBUG = True


Environment = ['prod', 'beta', 'dev', 'st', 'qa']

# salt auth
auth_content = ['vi', 'vim', 'poweroff', 'shutdown', 'rm', 'init', 'reboot', 'useradd', 'userdel', 'userhelper',
                'usermod', 'usernetctl', 'users', "echo"]

# LOGIN_URL = "http://auth.jumeird.com/api/login/?camefrom=jmops"
app_key = "&app_key=e00acc666d4911e3a268fa163e73f605"
app_name = "&app_name=jmops&key=1"
auth_url = "http://auth.xxx.com/"
auth_key = "e00acc666d4911e3a268fa163e73f605"

# 跳板机使用
springboard = "ea76757b5d91c5c96bf58500a5f7eda0"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # 'NAME': 'voilet_cmdb_v1',  # Or path to database file if using sqlite3.
        'NAME': 'cmdb_bc',  # Or path to database file if using sqlite3.
         'USER': 'root',
         'PASSWORD': 'Bc1366#7',  # Not used with sqlite3.
        'HOST': '192.168.1.191',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
        "OPTIONS": {
            "init_command": "SET foreign_key_checks = 0;",
        },
    },
}

# Zabbix
zabbix_on = False
zabbix_url = 'http://zabbix.360pai.test'
zabbix_user = 'admin'
zabbix_passwd = 'zabbix'



