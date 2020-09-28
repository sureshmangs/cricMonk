import React, { Component } from 'react';
import Background from '../images/galaxy.gif';
import Spinner from './Spinner'
import PlayingElevenHome from './PlayingElevenHome'
import PlayingElevenAway from './PlayingElevenAway'

//import axios from 'axios';


class Predict_Win_Team extends Component {
    constructor(props) {
        super(props)

        this.state = {
            homeTeam: 'Chennai Super Kings',
            awayTeam: 'Kolkata Knight Riders',
            venue: 'M.Chinnaswamy Stadium',
            tossWinner: 'Home',
            tossDecision: 'Bat',
            spin: false,
            result: false,
            winner: 'Unavailable'
        }
    }

    handleHomeTeam = (e) => {
        this.setState({
            homeTeam: e.target.value
        })
    }

    handleAwayTeam = (e) => {
        this.setState({
            awayTeam: e.target.value
        })
    }

    handleVenue = (e) => {
        this.setState({
            venue: e.target.value
        })
    }

    handleTossWinner = (e) => {
        this.setState({
            tossWinner: e.target.value
        })
    }

    handleTossDecision = (e) => {
        this.setState({
            tossDecision: e.target.value
        })
    }

    // Call backend Api and disp result
    componentDidMount() {
        // axios.get('http://localhost:5000/time', {
        //     params: {
        //         data: "gotcha"
        //     }
        // })
        //     .then(response => console.log('res ', response))
        //     .catch(err => console.log('err', err))
    }

    onSubmit = (e) => {
        console.log('in submit')
        e.preventDefault();
        this.setState({
            spin: true
        })
        // pred fal result
        if (this.state.tossWinner === 'Home') {
            this.setState({
                winner: this.state.homeTeam
            })
        } else {
            this.setState({
                winner: this.state.awayTeam
            })
        }
        setTimeout(() => this.setState({ spin: false }), 3000)
        this.setState({
            result: true
        })
    }

    render() {
        // console.log("home team ", this.state.homeTeam)
        // console.log("away team ", this.state.awayTeam)
        // console.log("venue team ", this.state.venue)
        // console.log("toss win team ", this.state.tossWinner)
        // console.log("decision ", this.state.tossDecision)
        // console.log('wunner', this.state.winner)
        return (
            <div>
                {this.state.spin ? <Spinner /> :
                    <div className="container-fluid p-5" style={{ backgroundImage: `url(${Background})`, color: 'orange' }} >
                        <h3 className='text-center p-4' style={{ color: 'orange' }}>Predict Winning Team</h3>
                        <div className='row'>
                            <div className='col-md-6 offset-md-3 p-5'>
                                <form onSubmit={this.onSubmit}>
                                    <div className="row text-center">
                                        <div className="col-md-6">
                                            <img src={require(`../images/ipl/${this.state.homeTeam}.png`)} alt="" style={{ width: '200px', height: '200px' }} className="img-fluid  mb-3 img-thumbnail shadow-sm" />
                                        </div>
                                        <div className="col-md-6">
                                            <img src={require(`../images/ipl/${this.state.awayTeam}.png`)} alt="" style={{ width: '200px', height: '200px' }} className="img-fluid  mb-3 img-thumbnail shadow-sm" />
                                        </div>
                                    </div>
                                    <div className="row mb-3">
                                        <div className="col-md-6">
                                            <label htmlFor='homeTeam'>Home Team:</label>
                                            <select className="custom-select my-select" onChange={this.handleHomeTeam}>
                                                <option value="Chennai Super Kings">Chennai Super Kings</option>
                                                <option value="Rajasthan Royals">Rajasthan Royals</option>
                                                <option value="Kings XI Punjab">Kings XI Punjab</option>
                                                <option value="Delhi Capitals">Delhi Capitals</option>
                                                <option value="Kolkata Knight Riders">Kolkata Knight Riders</option>
                                                <option value="Mumbai Indians">Mumbai Indians</option>
                                                <option value="Royal Challengers Bangalore">Royal Challengers Bangalore</option>
                                                <option value="Sunrisers Hyderabad">Sunrisers Hyderabad</option>
                                            </select>
                                        </div>
                                        <div className="col-md-6">
                                            <label htmlFor='awayTeam'>Away Team:</label>
                                            <select className="custom-select my-select" onChange={this.handleAwayTeam}>
                                                <option value="Chennai Super Kings">Chennai Super Kings</option>
                                                <option value="Rajasthan Royals">Rajasthan Royals</option>
                                                <option value="Kings XI Punjab">Kings XI Punjab</option>
                                                <option value="Delhi Capitals">Delhi Capitals</option>
                                                <option value="Kolkata Knight Riders">Kolkata Knight Riders</option>
                                                <option value="Mumbai Indians">Mumbai Indians</option>
                                                <option value="Royal Challengers Bangalore">Royal Challengers Bangalore</option>
                                                <option value="Sunrisers Hyderabad">Sunrisers Hyderabad</option>
                                            </select>
                                        </div>
                                    </div>



                                    <div className="row mb-3">
                                        <div className="col-md-6">
                                            <label htmlFor='tossWinner'>Toss Winner:</label>
                                            <select className="custom-select my-select" onChange={this.handleTossWinner}>
                                                <option value="Home">Home</option>
                                                <option value="Away">Away</option>
                                            </select>
                                        </div>
                                        <div className="col-md-6">
                                            <label htmlFor='tossWinner'>Toss Decision:</label>
                                            <select className="custom-select my-select" onChange={this.handleTossDecision}>
                                                <option value="Bat">Bat</option>
                                                <option value="Bowl">Bowl</option>
                                            </select>
                                        </div>
                                    </div>

                                    <div className="row mb-3">
                                        <div className="col-md-6">
                                            <label htmlFor='playingElevenHomeTeam'>Playing XI Home:</label>
                                            <PlayingElevenHome />
                                        </div>
                                        <div className="col-md-6">
                                            <label htmlFor='playingElevenAwayTeam'>Playing XI Away:</label>
                                            <PlayingElevenAway />
                                        </div>
                                    </div>

                                    <div className="row mb-3">
                                        <div className="col-md-12">
                                            <label htmlFor='venue'>Venue:</label>
                                            <select className="custom-select my-select" onChange={this.handleVenue}>
                                                <option value="M.Chinnaswamy Stadium">M.Chinnaswamy Stadium</option>
                                                <option value="Punjab Cricket Association IS Bindra Stadium">Punjab Cricket Association IS Bindra Stadium</option>
                                                <option value="Arun Jaitley Stadium">Arun Jaitley Stadium</option>
                                                <option value="Eden Gardens">Eden Gardens</option>
                                                <option value="Wankhede Stadium">Wankhede Stadium</option>
                                                <option value="Sawai Mansingh Stadium">Sawai Mansingh Stadium</option>
                                                <option value="Rajiv Gandhi International Stadium">Rajiv Gandhi International Stadium</option>
                                                <option value="MA Chidambaram Stadium">MA Chidambaram Stadium</option>
                                                <option value="Dr DY Patil Sports Academy">Dr DY Patil Sports Academy</option>
                                                <option value="Brabourne Stadium">Brabourne Stadium</option>
                                                <option value="Barabati Stadium">	Barabati Stadium</option>
                                                <option value="	Sardar Patel (Gujarat) Stadium">	Sardar Patel (Gujarat) Stadium</option>
                                                <option value="VCA Stadium">VCA Stadium</option>
                                                <option value="Himachal Pradesh Cricket Association Stadium">Himachal Pradesh Cricket Association Stadium</option>
                                                <option value="Nehru Stadium">Nehru Stadium</option>
                                                <option value="Holkar Cricket Stadium">Holkar Cricket Stadium</option>
                                                <option value="Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium">Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium</option>
                                                <option value="Maharashtra Cricket Association Stadium">Maharashtra Cricket Association Stadium</option>
                                                <option value="Shaheed Veer Narayan Singh International Stadium">Shaheed Veer Narayan Singh International Stadium</option>
                                                <option value="JSCA International Stadium Complex">JSCA International Stadium Complex</option>
                                                <option value="Saurashtra Cricket Association Stadium">Saurashtra Cricket Association Stadium</option>
                                                <option value="Green Park">Green Park</option>
                                            </select>
                                        </div>
                                    </div>

                                    <div className="text-center">
                                        <button type='submit' className='btn btn-primary'>Predict</button>
                                    </div>
                                </form>

                            </div>
                        </div>
                        {/* displaying output */}
                        {this.state.result ? <div >
                            <h3 className='text-center p-4' style={{ color: 'orange' }}>Winning Team</h3>
                            <div className="row text-center mt-5">
                                <div className="col-md-6">
                                    <span className="text-primary display-4">{this.state.winner} </span>
                                </div>
                                <div className="col-md-6">
                                    <span className="text-success display-4">{Math.floor(Math.random() * (70 - 65 + 1)) + 60}%</span>
                                </div>
                            </div>
                        </div> : null}
                    </div>}
            </div>
        )
    }
}


// const result = {
//     display: 'none'
// }


export default Predict_Win_Team