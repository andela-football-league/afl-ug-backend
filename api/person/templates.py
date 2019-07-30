def person_obj(person):
    return {
        "person_id": person.person_id,
        "first_name": person.first_name,
        "last_name": person.last_name,
        "nick_name": person.nick_name,
        "email": person.email,
        "picture": person.picture,
        "role": person.role,
        "team_id": person.team_id,
        "active": person.active,
        "links": [
            {"rel": "self", "href": f"/persons/{person.person_id}"},
            {"rel": "team", "href": f"/teams/{person.team_id}"},
        ],
    }


def persons_obj(persons):
    persons_obj = []
    for person in persons:
        persons_obj.append(person_obj(person))
    return persons_obj
