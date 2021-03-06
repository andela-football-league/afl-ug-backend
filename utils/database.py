from application import db


class DatabaseUtils(object):
    def save(self):
        """Utility method for saving new objects"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Utility method for deleting objects"""
        db.session.delete(self)
        db.session.commit()
