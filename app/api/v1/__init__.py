from flask import Blueprint


from app.api.v1 import session, contest, oj, spider


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    session.api.register(bp_v1)
    contest.api.register(bp_v1)
    oj.api.register(bp_v1)
    spider.api.register(bp_v1)
    return bp_v1