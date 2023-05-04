from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    step = IntegerField('Step', validators=[DataRequired()])
    step_target = IntegerField('Step Target', validators=[DataRequired()])
    weight = DecimalField(
        'Weight', validators=[DataRequired()])
    weight_target = DecimalField(
        'Weight Target', validators=[DataRequired()])
    height = DecimalField('Height', validators=[DataRequired()])
    submit = SubmitField('Submit')
