import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchOdds } from '../features/odds/oddsSlice';
import { Card, Table, Alert, Spinner } from 'react-bootstrap';

const Odds = ({ gameId }) => {
    const dispatch = useDispatch();
    const odds = useSelector((state) => state.odds.odds);
    const status = useSelector((state) => state.odds.status);
    const error = useSelector((state) => state.odds.error);

    useEffect(() => {
        if (status === 'idle' || gameId !== odds.gameId) {
            dispatch(fetchOdds(gameId));
        }
    }, [status, dispatch, gameId, odds.gameId]);

    const renderContent = () => {
        if (status === 'loading') {
            return <Spinner animation="border" role="status"><span className="visually-hidden">Loading...</span></Spinner>;
        }

        if (status === 'failed') {
            return <Alert variant="danger">{error}</Alert>;
        }

        if (status === 'succeeded' && odds.data) {
            return (
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>Bookmaker</th>
                            <th>Moneyline</th>
                            <th>Spread</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        {odds.data.map((odd, index) => (
                            <tr key={index}>
                                <td>{odd.bookmaker}</td>
                                <td>{odd.moneyline}</td>
                                <td>{odd.spread}</td>
                                <td>{odd.total}</td>
                            </tr>
                        ))}
                    </tbody>
                </Table>
            );
        }

        return null;
    };

    return (
        <Card>
            <Card.Body>
                <Card.Title>Odds for Game {gameId}</Card.Title>
                {renderContent()}
            </Card.Body>
        </Card>
    );
};

export default Odds;