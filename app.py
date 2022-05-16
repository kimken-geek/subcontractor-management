import os
from flask import Flask,render_template,request,redirect
from flask import abort
from model import db,SubcontractorsModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subcontract.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
 
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createsub.html')
 
    if request.method == 'POST':
        subcontractor_id = request.form['subcontractor_id']
        company = request.form['company']
        type = request.form['type']
        human_resources = request.form['human_resources']
        technical_rating = request.form['technical_rating']
        subcontractor = SubcontractorsModel(subcontractor_id=subcontractor_id, company=company, type=type, human_resources=human_resources, technical_rating=technical_rating)
        db.session.add(subcontractor)
        db.session.commit()
        return redirect('/data')
 
 
@app.route('/data')
def RetrieveSubs():
    subcontractors = SubcontractorsModel.query.all()
    return render_template('subcontractorlist.html',subcontractors = subcontractors)
 
 
@app.route('/data/<int:id>')
def RetrieveSubcontractor(id):
    subcontractor = SubcontractorsModel.query.filter_by(subcontractor_id=id).first()
    if subcontractor:
        return render_template('subcontractordata.html', subcontractor = subcontractor)
    return f"Subcontractor with id ={id} does not exist"
 
 
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    subcontractor = SubcontractorsModel.query.filter_by(subcontractor_id=id).first()
    if request.method == 'POST':
        if subcontractor:
            db.session.delete(subcontractor)
            db.session.commit()
            company = request.form['company']
            type = request.form['type']
            human_resources = request.form['human_resources']
            technical_rating = request.form['technical_rating']
            subcontractor = SubcontractorsModel(company=company, type=type, human_resources=human_resources, technical_rating=technical_rating)
            db.session.add(subcontractor)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Subcontractor with id = {id} Does not exist!"
 
    return render_template('update.html', subcontractor = subcontractor)
 
 
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    subcontractor = SubcontractorsModel.query.filter_by(subcontractor_id=id).first()
    if request.method == 'POST':
        if subcontractor:
            db.session.delete(subcontractor)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')
 
app.run(host='localhost', port=5000)