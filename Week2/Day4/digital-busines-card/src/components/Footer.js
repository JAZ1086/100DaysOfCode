import { FaTwitterSquare } from "react-icons/fa";
import {FaFacebookSquare } from "react-icons/fa";
import {FaInstagramSquare} from "react-icons/fa";
import {FaGithubSquare} from "react-icons/fa"

export default function Footer(){
    return(
        <footer className="footer">
            <div className="main-footer">
            <FaTwitterSquare className="footer-item"/>
            <FaFacebookSquare className="footer-item"/>
            <FaInstagramSquare className="footer-item"/>
            <FaGithubSquare className="footer-item"/>
            </div>
        </footer>
    )
}