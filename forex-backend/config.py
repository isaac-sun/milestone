import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://user:password@localhost/forex_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 邮件配置
    MAIL_SERVER = 'smtp.yeah.net'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('EMAIL_USER')
    MAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    MAIL_RECIPIENTS = ['scyys25@nottingham.edu.cn', 'scyzz24@nottingham.edu.cn']
    
    # 汇率API配置
    RATE_API_URL = "https://v6.exchangerate-api.com/v6/ef3a110ece1621c0293c7c53/latest/USD"
    UPDATE_INTERVAL = 1800  # 30分钟