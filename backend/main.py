# Last file we write because models.py tells us what sort of information we're going to be dealing with
#CRUD endpoints and the values we need to pass:

#Create:
#firstname, lastname, email, 
#Endpoint is the point after the / example: localhost:5000/create_contact
#Request Types: GET retrieve some inf, POST create something new, PATCH update something, DELETE

# the information is stored in JSON format 

from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts", methods=["GET"]) #endpoint + what do we want this function to do
def get_contacts():
    contacts = Contact.query.all() #get all the contacts from our database uising sqlalchemy
    #however we want this in json
    json_contacts = list(map(lambda contact: contact.to_json(), contacts)) #for every contact in contacts pass into our lambda (1 liner) function and convert to json
    return jsonify(json_contacts) #from list to JSON 

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    
    if not first_name or not last_name or not email:
        return jsonify(
            {
                "error": "Wrong Info"
            }
        ), 400 #400 is a bad request  
        
    new_contact = Contact(first_name = first_name, last_name = last_name, email = email)
    try:
        db.session.add(new_contact) #staged to database
        db.session.commit() #commit to database permananently
    except Exception as e:
        return jsonify(
            {
                "error": str(e)
            }
        ), 400
        
    return jsonify(
        {"Message": "Contact created successfully"}
        ), 201 #201 is created
    
    #Test API using tools like postman
    
@app.route("/update_contact/<int:user_id>", methods=["PATCH"]) #using id b/c its primary to identify user we want to update
def update_contact(user_id): #notice parameter is the same as path variable
    contact = Contact.query.get(user_id) #get contact by ID, similar to getter function in Java
        
    if not contact:
        return jsonify({"message": "Invalid ID"}), 404 #404 is not found
    
    data = request.json #get the data from the request, which is the new info (first name, last name email etc)
    contact.first_name = data.get("firstName", contact.first_name) #if we don't get a new first name, keep the old one
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)
    
    db.session.commit() #The contact object is already in the database, so we don't need to add it again, so commiting is enough
    
    return jsonify({"message": "Contact updated successfully"}) #can add 200, but thats default

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id) # get the user we want to delete
    
    if not contact:
        return jsonify({"message": "Invalid ID"}), 404
    
    db.session.delete(contact) #built in method to delete contact
    db.session.commit()
    
    return jsonify({
        "message": "Contact successfully deleted"
    })
        
if __name__ == '__main__':#if we run this filen not import, we want to run the app
    with app.app_context():
        db.create_all() #create the database if it doesn't exist
    
    app.run(debug=True)