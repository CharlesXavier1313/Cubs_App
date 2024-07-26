import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Provider } from 'react-redux';
import { store } from './store';
import Header from './components/Header';
import Odds from './components/Odds';
import BettingScores from './components/BettingScores';

const App = () => {
    const [gameId, setGameId] = useState(1);

    return (
        <Provider store={store}>
            <Router>
                <Header />
                <input 
                    type="number" 
                    value={gameId} 
                    onChange={(e) => setGameId(e.target.value)} 
                    placeholder="Enter Game ID" 
                />
                <Switch>
                    <Route path="/odds">
                        <Odds gameId={gameId} />
                    </Route>
                    <Route path="/betting-scores">
                        <BettingScores gameId={gameId} />
                    </Route>
                    <Route path="/">
                        <div>Welcome to the Cubs Betting Analytics App</div>
                    </Route>
                </Switch>
            </Router>
        </Provider>
    );
};

export default App;