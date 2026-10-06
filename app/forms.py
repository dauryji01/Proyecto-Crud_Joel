from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, number_range


class SuplementoForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    marca = StringField("Marca", validators=[DataRequired()])
    categoria = StringField("Categoría", validators=[DataRequired()])
    precio = FloatField("Precio", validators=[DataRequired(),number_range(min=0, message= "No se pueden cantidades negativas")])
    cantidad = IntegerField("Cantidad", validators=[DataRequired(),number_range(min=0, message= "No se pueden cantidades negativas")])
    
    submit = SubmitField("Guardar")