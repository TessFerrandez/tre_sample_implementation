from tre_api.database import db


class Schema(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    format = db.Column(db.String(20))
    schema = db.Column(db.String(200))
    version = db.Column(db.String(20))
    resource_type = db.Column(db.String(20))

    def __init__(self, schema_id: str):
        self.id = schema_id

    def __repr__(self):
        return '<Schema %r>' % self.id
