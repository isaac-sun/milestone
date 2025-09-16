from flask import Flask, jsonify
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
from models import db, ExchangeRate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# 初始化组件
db.init_app(app)
mail = Mail(app)

# 汇率获取函数
def fetch_exchange_rates():
    try:
        response = requests.get(Config.RATE_API_URL)
        data = response.json()
        
        with app.app_context():
            for pair in ['USD/CNY', 'EUR/USD']:
                rate = data['rates'][pair.split('/')[0]]
                entry = ExchangeRate(
                    currency_pair=pair,
                    rate=rate
                )
                db.session.add(entry)
            db.session.commit()
            
            # 发送邮件
            send_rate_alert(rate)
            
    except Exception as e:
        app.logger.error(f"汇率更新失败: {str(e)}")

# 邮件发送函数
def send_rate_alert(current_rate):
    msg = Message(
        subject='今日汇率提醒',
        sender=app.config['MAIL_USERNAME'],
        recipients=[app.config['MAIL_USERNAME']]
    )
    
    body = f"""
    今日最新汇率：
    USD/CNY: {current_rate}
    EUR/USD: {current_rate['EUR/USD']}
    """
    
    msg.body = body
    with app.app_context():
        mail.send(msg)

# 创建数据库表
@app.before_first_request
def create_tables():
    db.create_all()

# API路由
@app.route('/api/rates', methods=['GET'])
def get_rates():
    rates = ExchangeRate.query.order_by(ExchangeRate.timestamp.desc()).limit(100).all()
    return jsonify([r.to_dict() for r in rates])

# 定时任务配置
scheduler = BackgroundScheduler()
scheduler.add_job(fetch_exchange_rates, 'interval', seconds=Config.UPDATE_INTERVAL)
scheduler.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)