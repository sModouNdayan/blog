from flask import Flask, render_template,abort
#from mocks import Post
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ ='posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)

    def __repr__(self):
        return "<Post '{}'>".format(self.title)

@app.context_processor
def inject_time():
    return dict(now= datetime.now())

@app.context_processor
def utility_processor():
    def pluralize(count,singular,plural=None):
        
        if not isinstance(count,int):
            raise ValueError("{} must be an integer ".format(count))

        if plural is None:
            plural=singular + 's'
        if count == 1:
            string=singular
        else:
             string=plural
        return "{} {} ".format(count,string)   

    return dict(pluralize=pluralize)     

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')   

@app.route('/alkhouran')
def alkhouran():
    return render_template('pages/alkhouran.html') 

@app.route('/khassida')
def khassida():
    return render_template('pages/khassida.html')    

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404 

@app.route('/blog')
def posts_index():
    posts=Post.query.all()
    return render_template('posts/index.html',posts=posts)    


@app.route('/blog/posts/<int:id>')
def posts_show(id):
   post=Post.query.get(id)
   if post is None:
       abort(404)
   return render_template('posts/show.html',post=post)    

if __name__=='__main__':
    db.create_all()
    app.run(debug=True, port=3000)