import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("/names").then(
      res => res.json()
    ).then(
      data => {
        setData(data);
        console.log(data);
      }
    );
  }, []);

  return (

<div>
    {(typeof data.names === 'undefined')?(
      <p>Loading...</p>
      ):(
    <select>{
         (
    data.names.map((name , i )=>(
      <option key={i}>{name}</option>)))}
    </select>
)}
</div>
    );
}

export default App;