from flask import jsonify, make_response
from flask.views import MethodView
from webargs.flaskparser import use_args

from person.models import Person
from person.schema import PersonSchema
from person.templates import person_obj, persons_obj


class PersonView(MethodView):
    
    def get(self, person_id):
        if person_id:
            person = Person.query.filter_by(person_id=person_id).first()
            response = {
                "result": "ok",
                "person": person_obj(person)
            }
        else:
            persons = Person.query.all()
            # print(persons.query())
            response = {
                "result": "ok",
                "persons": persons_obj(persons)
            }
        return make_response(jsonify(response), 200)
    
    @use_args(PersonSchema(), locations=("json", "form"))
    def post(self, args):
        person = Person()
        for key, value in args.items():
            setattr(person, key, value)
        person.save()
        response = {
            "result": "ok",
            "person": person_obj(person)
        }
        return make_response(jsonify(response), 201)
