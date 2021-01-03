#encoding: utf-8
from flask import  Flask,render_template
#import  config
import  pymysql

from flask_sqlalchemy import  SQLAlchemy
app = Flask(__name__)
#app.config.from_object(config)

conn= pymysql.connect(host='rm-uf6gi7921ip08otlvqo.mysql.rds.aliyuncs.com', user='lijinqi',password='Quchaoyue6', db ='tianqidb',port=3306, charset='utf8')

print('连接数据库成功！')
cursor = conn.cursor()


@app.route('/')
def index():
    sql="select * from tianqi_tb"
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data[:]:
        print(i)

   # case = Tianqi.query.filter(tianqi_tb.id == 1)[0]
    cursor.close()
    conn.close()
    #return render_template('index.html',shijian=case.year,wendu=case.temp)
    return 's'
@app.route('/add')
def  add():
    return render_template('add.html')

@app.route('/view')
def  view():
    return render_template('view.html')

@app.route('/predict')
def  predict():
    return '这是预测页面'

if __name__=='__main__':

    app.run(debug=True)