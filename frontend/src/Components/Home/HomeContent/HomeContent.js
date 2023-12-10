import './HomeContent.css';
import Textbox from './components/Textbox';

export default function HomeContent() {

    var user = "Sudesh";
    var company = "Sudesh";
    var doj = "Sudesh";

    return (
        <div >
            <div className='homecontent-container'>
                <p>Home</p>
            </div>
            <div className='info'>

                <Textbox text={"Username: "+user}/>

                    <div style={{'border-right': '2px solid white', 'border-left': '2px solid white'}}>
                        <Textbox text={"Company Name: " + company}/>
                    </div>

                <Textbox text={"Date of Joining: " + doj}/>

            </div> 
            <div className='all-contents'>
                <div className="bg-text" style={{ padding: "2px 10px 8px 10px", borderRadius: "10px" , "background-color":"black"}}>
                    <Textbox text='1 Devices Used' />
                </div>
                <div className="bg-text" style={{ padding: "2px 15px 8px 15px", borderRadius: "10px" , "background-color":"black"}}>
                    <Textbox text='2 Active Boilers' />
                </div>
                <div className="bg-text" style={{ padding: "8px 10px 8px 10px", borderRadius: "10px" , "background-color":"black"}}>
                    <Textbox text='Industry: Milk' />
                </div>
                <div className="bg-text" style={{ padding: "2px 10px 8px 10px", borderRadius: "10px" , "background-color":"black"}}>
                    <Textbox text='2 Days until analysis' />
                </div>
            </div>
        </div>
    )
}