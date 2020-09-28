import React, { Component } from 'react';
import { Link } from "react-router-dom";


class Navbar extends Component {
    render() {
        return (
            <div>
                <div className="navbar navbar-expand-md bg-dark navbar-dark pt-0 pb-0" >
                    <Link className="navbar-brand" to="/"><img src={require('../images/myLogo1.png')} alt="logo" /></Link>
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="collapsibleNavbar">
                        <ul className="navbar-nav ml-auto mr-5">
                            <li className="nav-item">
                                <Link className="nav-link" to="/About">ABOUT</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/Teams">TEAMS</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/Predict" >PREDICT</Link>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        );
    }
}

export default Navbar;