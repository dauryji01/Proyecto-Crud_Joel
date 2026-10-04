from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class SuplementoForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    marca = StringField("Marca", validators=[DataRequired()])
    categoria = StringField("Categoría", validators=[DataRequired()])
    precio = FloatField("Precio", validators=[DataRequired()])
    cantidad = IntegerField("Cantidad", validators=[DataRequired()])
    
    submit = SubmitField("Guardar")