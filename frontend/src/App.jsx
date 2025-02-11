import { useState, useEffect } from 'react'
import ContactList from './ContactList'
import './App.css'

function App() {
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    fetchContacts();
  }, []); //empty array means it only runs once

  const fetchContacts = async () =>{ //async b/c needs to wait to grab info from backend
    const response = await fetch("http://127.0.0.1:5000/contacts");
    const data = await response.json(); //converts response to json
    setContacts(data);
    console.log(data);
  } 

  return (
    <>
      <ContactList contacts = {contacts}/>
    </>
  )
}

export default App
