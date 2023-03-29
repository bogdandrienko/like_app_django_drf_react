import React from 'react';
import logo from './logo.svg';
import { Counter } from './features/counter/Counter';
import './App.css';
import axios from "axios";

function App() {
  async function getData(){

    const token = "ey1JhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgwMTAxMzY5LCJpYXQiOjE2ODAwOTg5NjksImp0aSI6IjNjMTU1MDRjODhhNDQzZWQ5OTg4ZWI2NDY0OTAzOThmIiwidXNlcl9pZCI6MzUyfQ.bKX8qjg9nkSZUgjxL0VI-5GR96nRz0QqY9y3Qzhl1BA"
    const headers = {
      "Authorization" : `Bearer ${token}`
    }

    const response = await axios.get("http://127.0.0.1:8000/get_data/", {headers})
    if (response.status === 401) {
      //
    }

    console.log("response: ", response)
  }


  return (
    <div className="App">

      <button onClick={getData}>GET DATA</button>

      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Counter />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <span>
          <span>Learn </span>
          <a
            className="App-link"
            href="https://reactjs.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            React
          </a>
          <span>, </span>
          <a
            className="App-link"
            href="https://redux.js.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Redux
          </a>
          <span>, </span>
          <a
            className="App-link"
            href="https://redux-toolkit.js.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Redux Toolkit
          </a>
          ,<span> and </span>
          <a
            className="App-link"
            href="https://react-redux.js.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            React Redux
          </a>
        </span>
      </header>
    </div>
  );
}

export default App;
