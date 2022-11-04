from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc).astimezone())
    last_updated = db.Column(db.DateTime, default=datetime.now(timezone.utc).astimezone())

    def __repr__(self) -> str:
        return '<Task %r>' % self.id

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method=='POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "Task could not be added"
    else:
        task = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=task)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "Task could not be deleted"

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task=Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        task.last_updated = datetime.now(timezone.utc).astimezone()
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Task could not be updated"
    else:
        return render_template('update.html', task=task)

if __name__=="__main__":
    app.run(debug=True)