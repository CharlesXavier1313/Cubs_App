import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchOdds } from '../features/odds/oddsSlice';

const Odds = ({ gameId }) => {
    const dispatch = useDispatch();
    const odds = useSelector((state) => state.odds.odds);
    const status = useSelector((state) => state.odds.status);
    const error = useSelector((state) => state.odds.error);

    useEffect(() => {
        if (status === 'idle') {
            dispatch(fetchOdds(gameId));
        }
    }, [status, dispatch, gameId]);

    return (
        <div>
            <h2>Odds for Game {gameId}</h2>
            {status === 'loading' && <p>Loading...</p>}
            {status === 'succeeded' && (
                <ul>
                    {odds.map((odd, index) => (
                        <li key={index}>{odd.bookmaker}: {odd.odds_value}</li>
                    ))}
                </ul>
            )}
            {status === 'failed' && <p>{error}</p>}
        </div>
    );
};

export default Odds;