import { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

const [response, setResponse] = useState("")

useEffect(() => {
  async function testEndpoint() {
    const response = await fetch('http://localhost:5000/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json' 
      }
    })
    const data = await response.json();
    setResponse(data.response);
  }
  testEndpoint();
}, [] )

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>RESPONSE: {response}</p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
