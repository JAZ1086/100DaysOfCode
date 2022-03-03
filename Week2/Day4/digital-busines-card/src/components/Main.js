import { FaEnvelope } from "react-icons/fa";
import {FaLinkedinIn } from "react-icons/fa";
export default function Main(){
    return (
        <div className="main">
            <h3>Azumah Joshua</h3>
            <h4>Software Enginneer</h4>
            <h5>azumah.website</h5>
           
            <div className="info">
                <div className="btn">
                <button className=" btn-email"><FaEnvelope/> Email</button>
                <button className="btn-linkedIn"><FaLinkedinIn/> LinkedIn</button>
                </div> 
            <h3>About</h3>
            <p>I'm a software engineer. Passionate about breaking and building things using all the technology at my disposal.</p>
            <h3>Intrests</h3>
            <p>Food expert. Music scholar. Reader. Internet fanatic. Bacon buff. Entrepreneur. Travel geek. Pop culture ninja. Coffee fanatic.</p> 
            </div>
        </div>
    )
}