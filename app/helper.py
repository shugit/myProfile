from app import login_manager
from models import User,Project

@login_manager.user_loader
def load_user(userid):
    return User.get(userid)

@login_manager.token_loader
def token_loader(token):
    return User.get(token)


def getProjects():
    return Project.query.order_by(Project.end_time.desc()).all()