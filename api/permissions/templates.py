def permission_obj(permission):
    return {
        "permission_id": permission.permission_id,
        "permission_name": permission.permission_name,
        "links": [
            {"rel": "self", "href": f"/permissions/{permission.permission_id}"}
        ]
    }


def permissions_obj(permissions):
    permissions_obj = []
    for permission in permissions:
        permissions_obj.append(permission_obj(permission))
    return permissions_obj
