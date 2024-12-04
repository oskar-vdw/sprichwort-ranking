from . import db  # Import the db object that is initialized in __init__.py

class swtable(db.Model):  # db.Model is the base class for all models
    __tablename__ = 'swtable'  # The name of the table in the database

    # Define columns for the User table
    id = db.Column(db.Integer, primary_key=True)  # A unique ID for each user
    content = db.Column(db.String(800), nullable=False)  # User's name (required)
    explanation = db.Column(db.String(900), nullable=False)  # User's email (required and unique)
    icon = db.Column(db.String(100), nullable=False)  # User's email (required and unique)
    matchesplayed = db.Column(db.Integer, nullable=False)  # User's email (required and unique)
    elo = db.Column(db.Integer, nullable=False)  # User's email (required and unique)

    
    def __repr__(self):
        return f"<Sprichwort {self.content}>"