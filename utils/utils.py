

class Utils:

    @staticmethod
    def check_id(item_id, entity):
        try:
            int(item_id)
        except ValueError:
            response = { "error": f"{entity} id should be an integer!"}
            return response
        return {}

    @staticmethod
    def return_response(obj, response_, func, entity):
        response = {
            "result": "ok",
            entity.lower(): func(obj)
        } if obj and not response_ else {
            "message": f"{entity} not found!"
        }

        return response
