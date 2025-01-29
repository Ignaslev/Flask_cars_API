from models import db, Projektas
from flask import Flask, render_template, request, redirect, url_for, jsonify
from serializers import ProjektasSchema
from flask_cors import CORS

app = Flask(__name__)

# fizinises db prijungimas, konfiguyracija
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projektai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inicijuojam db
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def homepage():
    return render_template('projektai.html')

@app.route('/api/allcars')
def api_allcars():
    all_projects = Projektas.query.all()
    projects_data = [ProjektasSchema.model_validate(project).model_dump() for project in all_projects]
    return jsonify(projects_data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
