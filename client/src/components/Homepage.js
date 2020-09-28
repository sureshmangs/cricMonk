import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Homepage extends Component {
    render() {
        return (
            <div>
                <div className="bd-example">
                    <div id="carouselExampleCaptions" className="carousel slide" data-ride="carousel">
                        <ol className="carousel-indicators">
                            <li data-target="#carouselExampleCaptions" data-slide-to="0" className="active"></li>
                            <li data-target="#carouselExampleCaptions" data-slide-to="1"></li>
                            <li data-target="#carouselExampleCaptions" data-slide-to="2"></li>
                        </ol>
                        <div className="carousel-inner">
                            <div className="carousel-item active">
                                <img src={require('../images/2_1200x700.jpg')} className="d-block w-100" alt="..." />
                                <div className="carousel-caption d-none d-md-block">
                                    <h5>Best Vs Best</h5>
                                    <p>IPL 2020 Suspended Till Further Notice</p>
                                </div>
                            </div>
                            <div className="carousel-item">
                                <img src={require('../images/1_1200x700.jpg')} className="d-block w-100" alt="..." />
                                <div className="carousel-caption d-none d-md-block">
                                    <h5>Game Banayega Name</h5>
                                    <p>IPL 2020 Suspended Till Further Notice</p>
                                </div>
                            </div>
                            <div className="carousel-item">
                                <img src={require('../images/4_1200x700.jpg')} className="d-block w-100" alt="..." />
                                <div className="carousel-caption d-none d-md-block">
                                    <h5>Ab Khel Bolega</h5>
                                    <p>IPL 2020 Suspended Till Further Notice</p>
                                </div>
                            </div>
                        </div>
                        <a className="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-slide="prev">
                            <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span className="sr-only">Previous</span>
                        </a>
                        <a className="carousel-control-next" href="#carouselExampleCaptions" role="button" data-slide="next">
                            <span className="carousel-control-next-icon" aria-hidden="true"></span>
                            <span className="sr-only">Next</span>
                        </a>
                    </div>
                </div>
                <section className="container-fluid m-5 p-5">
                    <div className="row mb-5">
                        <div className="col-lg-6 col-md-6 col-12 ">
                            <img src={require('../images/4_1200x700.jpg')} alt="Newyork" className="img-fluid" />
                        </div>
                        <div className="col-lg-6 col-md-6 col-12 ">
                            <blockquote class="blockquote blockquote-custom bg-white p-3 shadow rounded">
                                <h3 className="">Predict The Outcome</h3>
                                <hr className="w-25" />
                                <p class="mb-0 mt-2 font-italic">"It is not scientifically possible to accurately predict the outcome of an action. To suggest otherwise runs contrary to historical experience and the nature of war"</p>
                                <footer class="blockquote-footer pt-4 mt-4 border-top">
                                    <cite title="Source Title">Jim Mattis</cite>
                                </footer>
                            </blockquote>
                            <Link to="/Predict"><button className="btn bg-primary text-white">Predict</button></Link>
                        </div>
                    </div>
                </section>
            </div>
        )
    }
}

export default Homepage
