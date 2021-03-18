from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, Email



class PropertyForm(FlaskForm):
    title=StringField('Property Title', validators=[InputRequired()])
    desc=TextAreaField('Description',validators=[InputRequired()])
    bedrooms=StringField('No. of Bedrooms', validators=[InputRequired()])
    bathrooms=StringField('No. of Bathrooms', validators=[InputRequired()])
    price=StringField('Price', validators=[InputRequired()])
    type = SelectField('House/ Apartment', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    location=StringField('Location', validators=[InputRequired()])     
    photo= FileField('Photo',validators=[FileRequired()])

    