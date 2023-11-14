import React, { useState, useEffect } from "react";
import "./App.css"

import {Header , Footer , Container} from './Components/index'

function App (){

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

  const [imageSrc, setImageSrc] = useState('');
  const [Price, SetPrice] = useState('');
  const [Ratings, SetRatings] = useState('');
  const [Corpus, SetCorpus] = useState('');

  const handleSaveClick = () => {
    fetch('/save_selected_value', {
      method:['POST'],
      headers: {
        'Content-Type':'application/json'},
        body:JSON.stringify({selectedValue})
      }).then(response => response.json()).then(data =>{
        setImageSrc(data.URL)
        SetPrice(data.Price)
        SetRatings(data.Ratings)
        SetCorpus(data.Corpus)
      });
  };






  return(
<>    



  <>

      <Header text={selectedValue} url={imageSrc}/>
      <Container>hi</Container>
      <Footer/>


  </>




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
      <div>
      <button onClick={handleSaveClick}>Save</button>
 
      {imageSrc && <img src={imageSrc} alt="Image"/>}
      </div>
      <p>{Corpus}</p>
      <p>{Price}</p>
      <p>{Ratings}</p>


  </div>


</>

  );
}
export default  App;
