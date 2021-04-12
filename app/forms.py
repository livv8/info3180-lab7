from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea



class MyForm(FlaskForm):
    descriptionn = TextArea('Description', validators=[DataRequired()])
    
class PhotoForm(FlaskForm):
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
    
    
''''
<form action="/process" method="post">
    <div>
        <label for="name">Full Name:</label>
        <input type="text" id="name" name="full_name" />
    </div>
    <div>
        <label for="mail">E-mail:</label>
        <input type="email" id="mail" name="email" />
    </div>
    <div>
        <label for="msg">Message:</label>
        <textarea id="msg" name="message"></textarea>
    </div>
        n type="submit">Send Message </button>
</form>
'''