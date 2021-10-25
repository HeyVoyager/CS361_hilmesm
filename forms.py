from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

# (-124.848974, 24.396308) - (-66.885444, 49.384358)

# def is_location(form, field):
#     field.data.replace(" ", "")
#     if ',' in field.data:
#         if '9' > field.data[0] > '0':
#             lat_lon = field.data.split(',')
#             if float(lat_lon[0]) > 49.384358 or float(lat_lon[0]) < 24.396308:
#                 raise ValidationError('Invalid Lat/Long')
#             elif float(lat_lon[1]) > -66.885444 or float(lat_lon) < -124.848974:
#                 raise ValidationError('Invalid Lat/Long')
#         else:
#             city_state = field.data.split(',')
#             if len(city_state[1]) != 2:
#                 raise ValidationError('Invalid City, State')
#     else:
#         if len(field.data) > 5:
#             raise ValidationError('Invalid zip code')


class SearchForm(FlaskForm):
    location = StringField('Location',
                           validators=[DataRequired(), Length(min=5, max=40)])
    submit = SubmitField('Submit')