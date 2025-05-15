from flask import Blueprint, render_template
from app.models import paises

main_routes= Blueprint('main', __name__)


@main_routes.route('/')
def index():
    data = paises()
    return render_template('index.html', paises=data)

