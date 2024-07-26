import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
    return (
        <header>
            <h1>Cubs Betting Analytics</h1>
            <nav>
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/odds">Odds</Link></li>
                    <li><Link to="/betting-scores">Betting Scores</Link></li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
