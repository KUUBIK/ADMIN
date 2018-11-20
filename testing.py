
from flask import Flask, render_template, session, request, json, jsonify, url_for, Markup, redirect
from flask_pymongo import PyMongo
import pymongo
import random

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)
user = mongo.db.users

# user.insert([{
#   "_id": 1,
#   "url": "static/forms/blog.html",
#   "img": "static/img/bg.jpg",
#   "img-src": "static/img/bg.jpg",
#   "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
#   "video": "static/video/vid.mp4",
#     "token": 3
#     }])

#          # {"_id": 2 ,'car2' : '/home/robert/androidflask/flaskled/tumblelog/photos/car2.png'},
#          # {"_id": 3 ,'car3': '/home/robert/androidflask/flaskled/tumblelog/photos/car3.png'}])
#     for men in user.find({"_id": 1}):
#         print (men)
#     with open('test/json/dat.json', 'w') as dat:
#        jsn = json.dump(men, dat, indent=2, ensure_ascii=False )
#     print(jsn)
#     return jsonify(men)
#
@app.route('/ok')
def my_form():
    return render_template ('index.html')

@app.route('/ok', methods=['GET' ,'POST'])
def my_form_post():
    text = request.form['title']
    processed_text = text
    # print (processed_text)
    num = random.random()
    title1 = [{'_id':num ,'title' : processed_text, 'name':'Rob'}]
    # print(title1)
    car = request.form['image']
    car_proc = car
    # print (car_proc)
    uri = 'static/img/' + car
    nums = random.random()
    url = [{'_id':nums ,'url_img' : uri, 'name':'Rob'}]
    # print(url)
    vid = request.form['video']
    video_1 = vid
    # print(video_1)
    urii = 'static/vid/' + vid

    texts = request.form['texts']
    texts_1 = texts
    rad = request.form['radio']
    if rad == 'yes':
        frid = 1
    if rad == 'no':
        frid = 2
    if rad == 'ok':
        frid = 3

    numb = random.random()
    urll = [{'_di':numb, 'url_vid': urii}]
    yse = [{'_id':num, 'img':uri, 'title' : processed_text,'url_vid':urii, '_token': frid, 'text':texts}]
    user.insert(yse)
    for mep in user.find({'_id':num}): #ищет по Id
        print (mep)
    with open('static/data.json', 'w') as dat: # открывает json файл "W"- это команда на запись (write, read)
       jsn = json.dump(yse, dat, indent=2, ensure_ascii=False ) # mep это значение которому присвоено наше json значение из монги

@app.route('/')
def ok():
    return render_template('zip.html')


  #   jsu = [{
  # "url-img": "static/img/1.jpg",
  # "img-src": "static/img/1.png",
  # "url-video": "static/video/vid.mp4",
  #   'Token': 'Fuck'
  #   }]
  #   user.updateOne(jsu)
  #   return ('Good!')





if __name__ == '__main__':
    app.run(host='192.168.8.100', port=8888,debug=True)
    # server = pywsgi.WSGIServer(('192.168.8.100', 8888), app, handler_class=WebSocketHandler)
    # server.serve_forever()

