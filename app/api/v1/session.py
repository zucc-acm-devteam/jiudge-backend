from flask_login import current_user, login_required, login_user, logout_user

from app.libs.error_code import Forbidden, DeleteSuccess, Success
from app.libs.red_print import RedPrint
from app.models.user import User
from app.validators.session import LoginForm

api = RedPrint('session')


@api.route('', methods=['GET'])
@login_required
def get_session_api():
    user = current_user
    user.fields = ['username', 'nickname', 'permission']
    return Success(data=user)


@api.route('', methods=['POST'])
def create_session_api():
    form = LoginForm().validate_for_api().data_
    user = User.get_by_id(form['username'])
    if user is None:
        return Forbidden('User not found')
    if not user.check_password(form['password']):
        return Forbidden('Wrong username or password')
    login_user(user, remember=True)
    return Success('Login successful')


@api.route('', methods=['DELETE'])
def delete_session_api():
    logout_user()
    return DeleteSuccess('Logout successful')
