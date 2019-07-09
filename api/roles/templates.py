def role_obj(role):
    return {
        "role_id": role.role_id,
        "role_name": role.role_name,
        "permission_id": role.permission_id,
        "links": [
            {"rel": "self", "href": f"/roles/{role.role_id}"}
        ]
    }


def roles_obj(roles):
    roles_obj = []
    for role in roles:
        roles_obj.append(role_obj(role))
    return roles_obj
