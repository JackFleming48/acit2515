from db import db

class User(db.Model):
    __tablename__ = "users"

    id = db.mapped_column(db.Integer, primary_key=True, autoincrement=True)
    name = db.mapped_column(db.String, nullable=False)
    phone = db.mapped_column(db.Integer, nullable=False)
    password = db.mapped_column(db.VARCHAR(255), nullable=False)
    create_date = db.mapped_column(db.DATETIME, default=db.datetime.now, nullable=False)

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | PASSWORD | Ph.: {self.phone} | Create Date: {self.create_date}"