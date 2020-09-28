import React, { Component } from 'react'

class Teams extends Component {
    render() {
        return (
            <div style={{ background: '#e8cbc0' }} className="pb-5">
                <div className="container py-5">
                    <div className="row text-center text-white">
                        <div className="col-lg-8 mx-auto">
                            <h1 className="display-4">Teams 2020</h1>
                        </div>
                    </div>
                </div>

                <div className="container">
                    <div className="row text-center">
                        <div className="col-lg-3 col-md-3 mb-4">
                            <div className=" shadow-sm py-3 px-3" style={{ background: '#fb8b0a' }}>
                                <img src={require('../images/ipl/Chennai Super Kings.png')} alt="" style={{ width: '200px', height: '200px' }} className="img-fluid mb-3 img-thumbnail shadow-sm" />
                                <h5 className="text-white mb-0">Chennai Super Kings</h5>
                                <p className="small text-white text-uppercase  pt-3">M. A Chidambaram Stadium</p>
                                <span className="small text-uppercase  badge p-2" style={{ background: '#a95e0b', color: '#d9d612' }}><i className="fa fa-trophy px-2"></i>2010, 2011, 2018</span>
                                <ul className="social mb-0 list-inline mt-3">
                                    <li className="list-inline-item"><a href="https://www.facebook.com" style={socialLink}><i className="fa fa-facebook-f"></i></a></li>
                                    <li className="list-inline-item"><a href="https://www.instagram.com" style={socialLink}><i className="fa fa-instagram "></i></a></li>
                                </ul>
                            </div>
                        </div>


                        <div className="col-lg-3 col-md-3 mb-4">
                            <div className=" shadow-sm py-3 px-3" style={{ background: '#01529d' }}>
                                <img src={require('../images/ipl/Delhi Capitals.png')} alt="" style={{ width: '200px', height: '200px' }} className="img-fluid  mb-3 img-thumbnail shadow-sm" />
                                <h5 className="text-white mb-0">Delhi Capitals</h5>
                                <p className="small text-white text-uppercase  pt-3">Feroz Shah Kotla Ground</p>
                                <span className="small text-uppercase  badge p-2" style={{ background: '#a95e0b', color: '#d9d612' }}><i className="fa fa-trophy px-2"></i></span>
                                <ul className="social mb-0 list-inline mt-3">
                                    <li className="list-inline-item"><a href="https://www.facebook.com" style={socialLink}><i className="fa fa-facebook-f"></i></a></li>
                                    <li className="list-inline-item"><a href="https://www.instagram.com" style={socialLink}><i className="fa fa-instagram "></i></a></li>
                                </ul>
                            </div>
                        </div>

                        <div className="col-lg-3 col-md-3 mb-4">
                            <div className=" shadow-sm py-3 px-3" style={{ background: '#8d2826' }}>
                                <img src={require('../images/ipl/Kings XI Punjab.png')} alt="" style={{ width: '200px', height: '200px' }} className="img-fluid  mb-3 img-thumbnail shadow-sm" />
                                <h5 className="text-white mb-0">Kings XI Punjab</h5>
                                <p className="small text-white text-uppercase  pt-3">IS Bindara Stadium</p>
                                <span className="small text-uppercase  badge p-2" style={{ background: '#a95e0b', color: '#d9d612' }}><i className="fa fa-trophy px-2"></i></span>
                                <ul className="social mb-0 list-inline mt-3">
                                    <li className="list-inline-item"><a href="https://www.facebook.com" style={socialLink}><i className="fa fa-facebook-f"></i></a></li>
                                    <li className="list-inline-item"><a href="https://www.instagram.com" style={socialLink}><i className="fa fa-instagram "></i></a></li>
                                </ul>
                            </div>
                        </div>

                        <div className="col-lg-3 col-md-3 mb-4">
                            <div className=" shadow-sm py-3 px-3" style={{ background: '#573373' }}>
                                <img src={require('../images/ipl/Kolkata Knight Riders.jpg')} alt="" style={{ width: '200px', height: '200px' }} className="img-fluid  mb-3 img-thumbnail shadow-sm" />
                                <h5 className="text-white mb-0">Kolkata Knight Riders</h5>
                                <p className="small text-white text-uppercase  pt-3">Eden Gradens</p>
                                <span className="small text-uppercase  badge p-2" style={{ background: '#a95e0b', color: '#d9d612' }}><i className="fa fa-trophy px-2"></i>2012, 2014</span>
                                <ul className="social mb-0 list-inline mt-3">
                                    <li className="list-inline-item"><a href="https://www.facebook.com" style={socialLink}><i className="fa fa-facebook-f"></i></a></li>
                                    <li className="list-inline-item"><a href="https://www.instagram.com" style={socialLink}><i className="fa fa-instagram "></i></a></li>
                                </ul>
                            </div>
                        </div>



                        <div className="col-lg-3 col-md-3 mb-4">
                            <div className=" shadow-sm py-3 px-3" style={{ background: '#004e87' }}>
                                <img src={require('../images/ipl/Mumbai Indians.png')} alt="" style={{ width: '200px', height: '200px' }} className="img-fluid  mb-3 img-thumbnail shadow-sm" />
                                <h5 className="text-white mb-0">Mumbai Indians</h5>
                                <p className="small text-white text-uppercase  pt-3">Wankhede Stadium</p>
                                <span className="small text-uppercase  badge p-2" style={{ background: '#a95e0b', color: '#d9d612' }}><i className="fa fa-trophy px-2"></i>2013, 2015, 2017, 2019</span>
                                <ul className="social mb-0 list-inline mt-3">
                                    <li className="list-inline-item"><a href="https://www.facebook.com" style={socialLink}><i className="fa fa-facebook-f"></i></a></li>
                                    <li className="list-inline-item"><a href="https://www.instagram.com" style={socialLink}><i className="fa fa-instagram "></i></a></li>
                                </ul>
                            </div>
                        </div>

                        <div className="col-lg-3 col-md-3 mb-4">
                            <div className=" shadow-sm py-3 px-3" style={{ background: '#233f7f' }}>
                                <img src={require('../images/ipl/Rajasthan Royals.png')} alt="" style={{ width: '200px', height: '200px' }} className="img-fluid mb-3 img-thumbnail shadow-sm" />
                                <h5 className="text-white mb-0">Rajasthan Royals</h5>
                                <p className="small text-white text-uppercase  pt-3">Sawai Mansingh Stadium</p>
                                <span className="small text-uppercase  badge p-2" style={{ background: '#a95e0b', color: '#d9d612' }}><i className="fa fa-trophy px-2"></i>2008</span>
                                <ul className="social mb-0 list-inline mt-3">
                                    <li className="list-inline-item"><a href="https://www.facebook.com" style={socialLink}><i className="fa fa-facebook-f"></i></a></li>
                                    <li className="list-inline-item"><a href="https://www.instagram.com" style={socialLink}><i className="fa fa-instagram "></i></a></li>
                                </ul>
                            </div>
                        </div>

                        <div className="col-lg-3 col-md-3 mb-4">
                            <div className=" shadow-sm py-3 px-3" style={{ background: '#262626' }}>
                                <img src={require('../images/ipl/Royal Challengers Bangalore.png')} alt="" style={{ width: '200px', height: '200px' }} className="img-fluid  mb-3 img-thumbnail shadow-sm" />
                                <h5 className="text-white text-truncate mb-0">Royal Challengers Bangalore</h5>
                                <p className="small text-white text-uppercase  pt-3">M Chinnaswammy Stadium</p>
                                <span className="small text-uppercase  badge p-2" style={{ background: '#a95e0b', color: '#d9d612' }}><i className="fa fa-trophy px-2"></i></span>
                                <ul className="social mb-0 list-inline mt-3">
                                    <li className="list-inline-item"><a href="https://www.facebook.com" style={socialLink}><i className="fa fa-facebook-f"></i></a></li>
                                    <li className="list-inline-item"><a href="https://www.instagram.com" style={socialLink}><i className="fa fa-instagram "></i></a></li>
                                </ul>
                            </div>
                        </div>

                        <div className="col-lg-3 col-md-3 mb-4">
                            <div className=" shadow-sm py-3 px-3" style={{ background: '#d63c30' }}>
                                <img src={require('../images/ipl/Sunrisers Hyderabad.jpg')} alt="" style={{ width: '200px', height: '200px' }} className="img-fluid  mb-3 img-thumbnail shadow-sm" />
                                <h5 className="text-white mb-0">Sunrisers Hyderabad</h5>
                                <p className="small text-white text-uppercase  pt-3">Rajiv Gandhi Stadium</p>
                                <span className="small text-uppercase  badge p-2" style={{ background: '#a95e0b', color: '#d9d612' }}><i className="fa fa-trophy px-2"></i>2016</span>
                                <ul className="social mb-0 list-inline mt-3">
                                    <li className="list-inline-item"><a href="https://www.facebook.com" style={socialLink}><i className="fa fa-facebook-f"></i></a></li>
                                    <li className="list-inline-item"><a href="https://www.instagram.com" style={socialLink}><i className="fa fa-instagram "></i></a></li>
                                </ul>
                            </div>
                        </div>



                    </div>
                </div>
            </div >
        )
    }
}


const socialLink = {
    width: '30px',
    height: '30px',
    border: '1px solid #ddd',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    color: '#666',
    borderRadius: '50%',
    transition: 'all 0.3s',
    fontSize: '0.9rem'
}


export default Teams
