import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import { Provider } from 'react-redux';
import { store } from './store';
import Header from './components/Header';
import Odds from './components/Odds';
import BettingScores from './components/BettingScores';
import WinLossChart from './components/WinLossChart';
import ControlPanel from './components/ControlPanel';
import BettingStats from './components/BettingStats';
import ErrorBoundary from './components/ErrorBoundary';
import { Container, Nav, Navbar, Form } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

const App = () => {
    const [gameId, setGameId] = useState(1);

    return (
        <Provider store={store}>
            <Router>
                <ErrorBoundary>
                    <Header />
                    <Navbar bg="light" expand="lg">
                        <Container>
                            <Navbar.Toggle aria-controls="basic-navbar-nav" />
                            <Navbar.Collapse id="basic-navbar-nav">
                                <Nav className="me-auto">
                                    <Nav.Link as={Link} to="/">Home</Nav.Link>
                                    <Nav.Link as={Link} to="/odds">Odds</Nav.Link>
                                    <Nav.Link as={Link} to="/betting-scores">Betting Scores</Nav.Link>
                                    <Nav.Link as={Link} to="/win-loss-chart">Win-Loss Chart</Nav.Link>
                                    <Nav.Link as={Link} to="/betting-stats">Betting Stats</Nav.Link>
                                    <Nav.Link as={Link} to="/control-panel">Control Panel</Nav.Link>
                                </Nav>
                                <Form className="d-flex">
                                    <Form.Control
                                        type="number"
                                        value={gameId}
                                        onChange={(e) => setGameId(e.target.value)}
                                        placeholder="Enter Game ID"
                                    />
                                </Form>
                            </Navbar.Collapse>
                        </Container>
                    </Navbar>
                    <Container className="mt-3">
                        <Switch>
                            <Route path="/odds">
                                <Odds gameId={gameId} />
                            </Route>
                            <Route path="/betting-scores">
                                <BettingScores gameId={gameId} />
                            </Route>
                            <Route path="/win-loss-chart">
                                <WinLossChart />
                            </Route>
                            <Route path="/betting-stats">
                                <BettingStats />
                            </Route>
                            <Route path="/control-panel">
                                <ControlPanel />
                            </Route>
                            <Route path="/">
                                <h1>Welcome to the Cubs Betting Analytics App</h1>
                                <p>Use the navigation menu to explore different features of the application.</p>
                            </Route>
                        </Switch>
                    </Container>
                </ErrorBoundary>
            </Router>
        </Provider>
    );
};

export default App;