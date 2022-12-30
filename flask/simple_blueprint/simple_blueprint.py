from flask import Blueprint

test_blueprint = Blueprint('test_blueprint', __name__, template_folder='templates', static_folder='static')

@test_blueprint.route('/')
def index():
    return "test route"