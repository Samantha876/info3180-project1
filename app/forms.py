from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, Email



class PropertyForm(FlaskForm):
    title=StringField('Title', validators=[InputRequired()])
    bedrooms=StringField('Bedrooms', validators=[InputRequired()])
    bathrooms=StringField('Bathrooms', validators=[InputRequired()])
    location=StringField('Location', validators=[InputRequired()])
    price=StringField('Price', validators=[InputRequired()])
    
    type = SelectField('House/ Apartment', choices=[('house', 'House'), ('apartment', 'Apartment')])
    desc=TextAreaField('Description',validators=[InputRequired()])
    photo= FileField('Photo',validators=[FileRequired(), FileAllowed(['jpg','png'])])
    