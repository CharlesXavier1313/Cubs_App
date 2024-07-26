import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchBettingScores } from '../features/bettingScores/bettingScoresSlice';

const BettingScores = ({ gameId }) => {
    const dispatch = useDispatch();
    const score = useSelector((state) => state.bettingScores.score);
    const status = useSelector((state) => state.bettingScores.status);
    const error = useSelector((state) => state.bettingScores.error);

    useEffect(() => {
        if (status === 'idle') {
            dispatch(fetchBettingScores(gameId));
        }
    }, [status, dispatch, gameId]);

    return (
        <div>
            <h2>Betting Score for Game {gameId}</h2>
            {status === 'loading' && <p>Loading...</p>}
            {status === 'succeeded' && <p>Score: {score}</p>}
            {status === 'failed' && <p>{error}</p>}
        </div>
    );
};

export default BettingScores;
