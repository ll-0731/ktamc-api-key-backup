# -*- coding: utf-8 -*-
"""
资管平台生产数据库配置
环境：production  T-M-20260901-03
"""

DB_CONFIG = {
    "host": "10.20.30.40",
    "port": 3306,
    "user": "assetadmin",
    "password": "Prod@2026#Abc!",       # 生产库账号密码
    "database": "keceamc_customer",
}

REDIS_CONFIG = {
    "host": "10.20.30.41",
    "port": 6379,
    "password": "redis2026kt",
    "db": 3,
}

# TODO: 上线前记得删除明文密码，改走KMS
