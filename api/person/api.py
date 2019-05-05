from flask import jsonify, make_response
from flask.views import MethodView
from webargs.flaskparser import use_args

from api.person.models import Person
from api.person.schema import PersonSchema
from api.person.templates import person_obj, persons_obj
from helpers.authentication import auth


class PersonView(MethodView):
    def get(self, person_id):
        if person_id:
            person = Person.query.filter_by(person_id=person_id).first()
            response = {"result": "ok", "person": person_obj(person)}
        else:
            persons = Person.query.all()
            response = {"result": "ok", "persons": persons_obj(persons)}
        return make_response(jsonify(response), 200)

    @use_args(PersonSchema(), locations=("json", "form"))
    def post(self, args):
        person = Person()
        for key, value in args.items():
            setattr(person, key, value)
        person.save()
        response = {"result": "ok", "person": person_obj(person)}
        return make_response(jsonify(response), 201)


class RegisterLoginView(MethodView):
    def post(self):
        user = Person()
        saved_user = auth.save_user(user)

        if not isinstance(saved_user, tuple):
            return saved_user

        if saved_user[0] and not saved_user[1]:
            response = {"result": "ok", "login": "Login successful"}
            return make_response(jsonify(response), 200)

        if saved_user[0] and saved_user[1]:
            response = {
                "result": "ok",
                "message": "Registration successful",
                "person": person_obj(saved_user[1]),
            }
            return make_response(jsonify(response), 201)
