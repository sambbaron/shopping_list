""" Add Test Data """

from werkzeug.security import generate_password_hash

from grocery_list.models import *
from grocery_list.database import session


def add_user():
    """ Add Test User """
    user = User(name="Testy",
                email="testy@test.com",
                password=generate_password_hash("test")
    )
    session.add(user)
    session.commit()


def add_store():
    """ Add Test Store

    Associated with test User from setUp
    """
    store = Store(name="Test Store", default=True)
    session.add(store)
    session.commit()


def add_user_store():
    """ Add Test UserStore association

    Associated with test User and Store
    """
    # Check for test User and Store
    if session.query(User).get(1) is None:
        add_user()
    if session.query(Store).get(1) is None:
        add_store()

    user_store = UserStore(user_id=1,
                           store_id=1,
                           nickname="My Test Store"
    )
    session.add(user_store)
    session.commit()


def add_route():
    """ Add Test Route

    Associated with test User and Store
    """
    # Check for test User and Store
    if session.query(User).get(1) is None:
        add_user()
    if session.query(Store).get(1) is None:
        add_store()

    route = Route(name="Full Shop",
                  default=True,
                  user_id=1, store_id=1
    )
    session.add(route)
    session.commit()


def add_list():
    """ Add Test List

    Associated with test User and Route
    """
    # Check for test User and Store
    if session.query(User).get(1) is None:
        add_user()
    if session.query(Route).get(1) is None:
        add_route()

    list = List(shop_date=datetime.date.today(),
                user_id=1,
                route_id=1
    )
    session.add(list)
    session.commit()