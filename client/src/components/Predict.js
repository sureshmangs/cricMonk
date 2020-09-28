import React, { Component } from 'react'
import { Link } from 'react-router-dom'
//import Background from '../images/galaxy.gif';
let Backg = "https://cdn.dribbble.com/users/375236/screenshots/4447887/cricket_yorker_dribbble.gif";
export class Predict extends Component {
    render() {
        return (
            <div className="container-fluid p-5" style={{ backgroundImage: `url(${Backg})`, color: 'orange' }} >
                <div className="container pb-5">
                    <div className="row text-center text-white">
                        <div className="col-lg-8 mx-auto">
                            <h1 style={{ color: "rgb(90 89 89)" }}>PREDICT</h1>
                        </div>
                    </div>
                </div>

                <div className="container">
                    <div className="row text-center">
                        <div className="col-lg-4 col-md-4 mb-4">
                            <div className="bg-white rounded shadow-sm py-5 px-4"><img src={require('../images/rocket.gif')} alt="" width="100" className="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm" />
                                <h5 className="mb-0">Winning Team</h5>
                                <Link to="/Predict_win_team"><button className="btn btn-success btn-sm mt-3" >Predict</button></Link>
                            </div>
                        </div>


                        <div className="col-lg-4 col-md-4 mb-4">
                            <div className="bg-white rounded shadow-sm py-5 px-4"><img src={require('../images/rocket.gif')} alt="" width="100" className="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm" />
                                <h5 className="mb-0">Runs Scored</h5>
                                <Link to="/Predict_score"><button className="btn btn-success btn-sm mt-3" >Predict</button></Link>
                            </div>
                        </div>


                        <div className="col-lg-4 col-md-4 mb-4">
                            <div className="bg-white rounded shadow-sm py-5 px-4"><img src={require('../images/rocket.gif')} alt="" width="100" className="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm" />
                                <h5 className="mb-0">Team Selection</h5>
                                <Link to="/Predict_select_team"><button className="btn btn-success btn-sm mt-3" >Predict</button></Link>
                            </div>
                        </div>

                    </div>
                </div>

            </div>
        )
    }
}





export default Predict
