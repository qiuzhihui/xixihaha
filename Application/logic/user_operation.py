import json

# user defined packages
from .import objects


def get_user_data(db, email):
    """
    get user data from database
    :param db: type object
    :param email: type str
    :return: dict
    """
    query = "select * from user where email = {lq}{email}{rq}".format(email=email,
                                                                      lq="'",
                                                                      rq="'")
    print("getting user with query", query)
    rows = db.basic_getter(query=query)
    result = {}
    if len(rows):
        row = rows[0]
        print(row)
        row = [str(x) for x in row]
        user = objects.User(id=row[0],
                            username=row[1],
                            email=row[2],
                            last_name=row[3],
                            first_name=row[4],
                            phone_number=row[5],
                            register_date=row[8])

        result = user.__dict__
    return json.dumps(result)


def set_user_data(db, data):
    """
    set user data to database
    :param db: type object
    :param data: type str
    :return: dict
    """
    if not isinstance(data, dict):
        data = json.loads(data)
        print(data)
    username = data["username"]
    email = data["email"]
    last_name = data["last_name"]
    first_name = data["first_name"]
    phone_number = data["phone_number"]
    password = data["password"]
    manage = "NULL"
    register_date = data["register_date"]
    query = "INSERT INTO user (username, email, last_name, first_name, phone_number, password, manage, register_date) " \
                "VALUES ({l}{}{r}, {l}{}{r}, {l}{}{r}, {l}{}{r}, {l}{}{r}, {l}{}{r}, {l}{}{r}, {l}{}{r});"\
            .format(username, email, last_name,first_name, phone_number, password, manage, register_date, l="'", r="'")
    print("query:\n", query)
    result = db.basic_setter(query=query)
    return str(result)
