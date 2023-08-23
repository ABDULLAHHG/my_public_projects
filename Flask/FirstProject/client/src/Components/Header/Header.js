import'./Header.css'

const Header = (props) => {
  return (
    <div>
      <nav class="navbar navbar-light bg-light">
        <a class="navbar-brand" href="#">
        {typeof props.url === "string" ? (
           <img src={props.url} width="30" height="30" class="d-inline-block align-top" alt=""/>
          ) : (
           <img src='' width="30" height="30" class="d-inline-block align-top" alt=""/>)}
        </a>
        <li><a>{props.text}</a></li>
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
      </nav>
    </div>
  )
}
export default Header
