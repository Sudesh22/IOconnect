import "./Card.css";
import mail_img from "./Mail.png";
import linkedin_img from "./linkedin.png";
export default function Card({ name, skill, webLink, img }) {
  return (
    <div className="card-dsn">
      <div className="card">
        <div className="profile">
          <img
            className="profile-img"
            src={`${process.env.PUBLIC_URL}/images/${img}`}
            alt="Profile"
          ></img>
          <h1 className="name">{name}</h1>
          <h4 className="skill">{skill}</h4>
          <p className="web-link">{webLink}</p>
          <div className="buttons">
            <button className="email">
              <img src={mail_img} alt="mail_icon"></img>
              <div>{"Email"}</div>
            </button>
            <button className="linkedin">
              <img src={linkedin_img} alt="linkedin_icon"></img>
              <div>{"LinkedIn"}</div>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
