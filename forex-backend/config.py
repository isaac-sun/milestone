import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://user:password@localhost/forex_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 邮件配置
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('EMAIL_USER')
    MAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    
    # 汇率API配置
    RATE_API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
    UPDATE_INTERVAL = 86400  # 24小时