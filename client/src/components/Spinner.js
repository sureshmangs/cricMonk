import React from 'react';
import Background from '../images/galaxy.gif';

function Spinner() {
    return (
        <div>
            <div className="container-fluid p-5" style={{ backgroundImage: `url(${Background})`, color: 'orange' }} >
                <h3 className='text-center p-4' style={{ color: 'orange' }}>Hang Up There</h3>
                <img
                    src={require('../images/spinner1.gif')}
                    style={spinStyle}
                    alt='Loading...' />
            </div>

        </div>
    )
}

const spinStyle = {
    width: '400px',
    height: '300px',
    margin: '200px auto 200px auto',
    display: 'block'
}
export default Spinner