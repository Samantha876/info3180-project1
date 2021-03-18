"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, flash
from .forms import PropertyForm
from werkzeug.utils import secure_filename
from app.models import PropertyMod
from app import db
from flask.helpers import send_from_directory


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/property',methods=['POST', 'GET'])
def property():
    """For displaying the form to add a new property."""
    form=PropertyForm()
    if request.method == 'POST' and form.validate_on_submit():
        title= form.title.data
        bedrooms=form.bedrooms.data
        bathrooms= form.bathrooms.data
        location= form.location.data
        price= form.price.data
        type= form.type.data
        desc= form.desc.data

        photo= form.photo.data
        filename= secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        property= PropertyMod(title,bedrooms,bathrooms,location,price,type,desc,filename)
        db.session.add(property)
        db.session.commit()
        

    return render_template('property.html', form=form)
    flash('Property was successfully added', 'success')
    
@app.route('/upload/<filename>')
def get_image(filename):
    root_dir=os.getcwd()
    return send_from_directory(os.path.join(root_dir,app.config['UPLOAD_FOLDER']),filename)
    
@app.route('/properties')
def properties():
    """For displaying a list of all properties in the database."""
    properties=PropertyMod.query.all()
    return render_template('properties.html',properties=properties)

@app.route('/property/<propertyid>')
def propertyid(propertyid):
    """For viewing an individual property by the specific property id. """
    propertyid=PropertyMod.query.get(propertyid)
    return render_template('propertyid.html', propertyid=propertyid)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
