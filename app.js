import './App.css';
import Button from 'react-bootstrap/Button'

function getUserEmail() {
  return "allen.averbukh@gmail.com";
}
// connnect with backend to retrieve current username email 

function App() {

  const text = "hello"
  
  return (
    <div className="App">
      <header className="App-header">
        <p >
          Create Appointment
        </p>
        <Button className = "Button">
          Edit 
        </Button>
        <Button className = "Button2">
          History
        </Button>
        
      </header>

      <header className = "Username">
        <p >
          Current User: {getUserEmail()}
        </p>
      </header>

    </div>
     
  );
}

export default App;
