from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired,FileAllowed

class UploadForm(FlaskForm):
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png','Images Only'])])