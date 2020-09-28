import React, { Component } from 'react'

class About extends Component {
    render() {
        return (
            <div style={{ background: '#e8cbc0' }} className="pb-5">
                <div className="container py-5">
                    <div className="row text-center text-white">
                        <div className="col-lg-8 mx-auto">
                            <h1 className="display-4">Meet the DEVs</h1>
                        </div>
                    </div>
                </div>


                <div className="container">
                    <div className="row text-center">
                        <div className="col-lg-4 col-md-4 mb-4">
                            <div className="bg-white rounded shadow-sm py-5 px-4"><img src={require('../images/shree.jpg')} alt="" width="100" className="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm" />
                                <h5 className="mb-0">Shreemohan Bajpai</h5><span className="small text-uppercase text-muted">Developer</span>
                                <ul className="social mb-0 list-inline mt-3">
                                    <li className="list-inline-item"><a href="undefiend" style={socialLink}><i className="fa fa-facebook-f"></i></a></li>
                                    <li className="list-inline-item"><a href="undefiend" style={socialLink}><i className="fa fa-github"></i></a></li>
                                    <li className="list-inline-item"><a href="undefiend" style={socialLink}><i className="fa fa-instagram"></i></a></li>
                                    <li className="list-inline-item"><a href="undefiend" style={socialLink}><i className="fa fa-linkedin"></i></a></li>
                                </ul>
                            </div>
                        </div>


                        <div className="col-lg-4 col-md-4 mb-4">
                            <div className="bg-white rounded shadow-sm py-5 px-4"><img src="https://instagram.fjdh2-1.fna.fbcdn.net/v/t51.2885-19/s150x150/95443415_2433984323304698_8839268318389993472_n.jpg?_nc_ht=instagram.fjdh2-1.fna.fbcdn.net&_nc_ohc=UKRwoiEinHkAX8L5Jlu&oh=ff1db0847068a591810e4107918de9e1&oe=5F4AF51D" alt="" width="100" className="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm" />
                                <h5 className="mb-0">Suresh Mangs</h5><span className="small text-uppercase text-muted">Developer</span>
                                <ul className="social mb-0 list-inline mt-3">
                                    <li className="list-inline-item"><a href="undefiend" style={socialLink}><i className="fa fa-facebook-f"></i></a></li>
                                    <li className="list-inline-item"><a href="undefiend" style={socialLink}><i className="fa fa-github"></i></a></li>
                                    <li className="list-inline-item"><a href="undefiend" style={socialLink}><i className="fa fa-instagram"></i></a></li>
                                    <li className="list-inline-item"><a href="undefiend" style={socialLink}><i className="fa fa-linkedin"></i></a></li>
                                </ul>
                            </div>
                        </div>


                        <div className="col-lg-4 col-md-4 mb-4">
                            <div className="bg-white rounded shadow-sm py-5 px-4"><img src="https://instagram.fjdh2-1.fna.fbcdn.net/v/t51.2885-19/s150x150/89824356_210261000054035_4629987655759691776_n.jpg?_nc_ht=instagram.fjdh2-1.fna.fbcdn.net&_nc_ohc=Y6zL_7WLDXsAX-_Ee9q&oh=c38141da95f09d4dc32a4a6261e16cdb&oe=5F4BD3A8" alt="" width="100" className="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm" />
                                <h5 className="mb-0">Jatin Verma</h5><span className="small text-uppercase text-muted">Developer</span>
                                <ul className="social mb-0 list-inline mt-3">
                                    <li className="list-inline-item"><a href="undefiend" style={socialLink}><i className="fa fa-facebook-f"></i></a></li>
                                    <li className="list-inline-item"><a href="undefiend" style={socialLink}><i className="fa fa-github"></i></a></li>
                                    <li className="list-inline-item"><a href="undefiend" style={socialLink}><i className="fa fa-instagram"></i></a></li>
                                    <li className="list-inline-item"><a href="undefiend" style={socialLink}><i className="fa fa-linkedin"></i></a></li>
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


export default About
