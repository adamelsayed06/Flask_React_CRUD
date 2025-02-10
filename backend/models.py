from config import db #local import of our database instance

#Create table named contact and the attributes we define (id, name email etc) are columns of this table
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    #db.Integer is the type of the column, primary_key=True
    #means this is 100% unique unlike something like a name 
    #which can overlap and is what we will primarily use to reference this row
    first_name = db.Column(db.String(80), unique=False, nullable = False) #max length = 80, dupe values allowed,can't pass null value
    last_name = db.Column(db.String(80), unique=False, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False) #no two same emails
    
    def to_json(self): 
        #self is the an instance of the contact class so we can convert to JSON for API
        return{
            "id": self.id,
            "firstName": self.first_name, #camelCase is conventional for JSON
            "lastName": self.last_name,
            "email": self.email
        }