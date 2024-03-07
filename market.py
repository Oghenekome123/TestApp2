from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
db=SQLAlchemy(app)

class Items(db.Model):
   id=db.Column(db.Integer(),nullable=False, primary_key=True)
   name=db.Column(db.String(length=54),nullable=False,unique=True)
   price=db.Column(db.Integer(),nullable=False)
   desc=db.Column(db.String(length=254),nullable=False)

def __repr__(self):
    return f"Item{self.name}"

@app.route('/')
@app.route('/home')
def home_page():
    items=[
        {"id":1,"name":"Laptop","Price":"500","desc":"HP"},
        {"id":2,"name":"Phone","Price":"100","desc":"Asus"},
        {"id":3,"name":"Mouse","Price":"50","desc":"Razer"}
    ]
    return render_template('home.html', items=items)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/shop', methods=['GET','POST'])
def shop_page():
    if request.method == "POST":
       product_name= request.form['Name']
       price=request.form['price']
       desc=request.form['desc']
       email=request.form['email']
       password=request.form['password']

       item=Items(name=product_name,price=price,desc=desc)
       print(f'Email:{email}, Password: {password}')
       return 'Submitted successfully'
       with app.app_context():
          db.session.add(item)
          db.session.commit()

       return redirect('/home')
    return render_template('shop.html')
