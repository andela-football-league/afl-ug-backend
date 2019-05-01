import jwt

from flask import jsonify, make_response, request
from sqlalchemy.exc import SQLAlchemyError


class Authentication:
    def get_token(self):
        try:
            token = request.headers["Authorization"].split()[1]
            return token
        except:
            pass

    def decode_token(self):
        try:
            auth_token = self.get_token()
            if not auth_token:
                response = {"error": "No token. Please provide a valid token!"}
                return make_response(jsonify(response), 401)
            user_payload = jwt.decode(auth_token, verify=False)
            return user_payload["UserInfo"]
        except jwt.ExpiredSignatureError:
            response = {"error": "Token has expired, please login again"}
            return make_response(jsonify(response), 401)
        except jwt.InvalidTokenError:
            response = {"error": "Invalid token, please provide a valid token"}
            return make_response(jsonify(response), 401)

    def save_user(self, user_obj):
        try:
            user_info = self.decode_token()
            if not isinstance(user_info, dict):
                return user_info
            user_details = {
                "email": user_info.get("email"),
                "first_name": user_info.get("first_name"),
                "last_name": user_info.get("last_name"),
                "name": user_info.get("name"),
                "picture": user_info.get("picture"),
            }
            user = user_obj.query.filter_by(email=user_info.get("email")).first()
            if user:
                return True, None
            if not user:
                for key, value in user_details.items():
                    setattr(user_obj, key, value)
                user_obj.save()
        except SQLAlchemyError:
            pass

        return True, user_obj


auth = Authentication()
