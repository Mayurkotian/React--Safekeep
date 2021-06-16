import './App.css';

function App() {
  return (
    <div className="App">
      <form className ="header-form">
        <input type="text" placeholder ="First Name"/>
        <input type="text" placeholder ="Last Name"/>
        <input type="text" placeholder ="Hours Worked"/>
        <button type="submit">Send</button>
      </form>
      <div className= "text-block">
        <h1>Participation Data App</h1>
        <p>This app creates, demonstrates, and deletes users and shows
            their percentage of participation
        </p>
      </div>
      <div className= "tables">
        
      </div>
      <div className = "graph">

      </div>

    </div>
  );
}

export default App;
