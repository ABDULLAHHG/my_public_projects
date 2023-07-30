import React, { useState, useEffect } from "react";

function App() {

  const [data, setData] = useState([{}]);
  const [selectedValue, setSelectedValue] = useState('');

  useEffect(() => {
    fetch("/names").then(
      res => res.json()
    ).then(
      data => {
        setData(data);
      }
    );
  }, []);


  const handleSelectChange = (event) => {
    setSelectedValue(event.target.value);

  };


  return (

<div>
    {(typeof data.names === 'undefined')?(
      <p>Loading...</p>
      ):(
    <select value={selectedValue} onChange={handleSelectChange} >{
         (
    data.names.map((name , i )=>(
      <option value={name}  key={i}>{name}</option>)))}
    </select>
    
)}
    <button onClick={() => {
          console.log(selectedValue);

        fetch('/save_selected_value', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          
          body: JSON.stringify({ selectedValue })
        });
  }}>Save</button>

</div>
    );
}

export default App;



