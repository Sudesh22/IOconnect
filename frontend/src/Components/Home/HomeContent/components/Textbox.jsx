import './Textbox.css';

export default function Textbox({text}){
    return(
        <div className='textbox-container'>
            <p>{text}</p>
        </div>
    )
}