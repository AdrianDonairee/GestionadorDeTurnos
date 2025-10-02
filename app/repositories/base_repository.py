from app import db

class Create:
    @staticmethod
    def add(instance):
        db.session.add(instance)
        db.session.commit()
        return instance

class Read:
    @staticmethod
    def get_by_id(model, id):
        return model.query.get(id)

    @staticmethod
    def get_all(model):
        return model.query.all()

class Update:
    @staticmethod
    def save():
        db.session.commit()

class Delete:
    @staticmethod
    def delete(instance):
        db.session.delete(instance)
        db.session.commit()
