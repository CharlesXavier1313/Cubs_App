import { configureStore } from '@reduxjs/toolkit';
import oddsReducer from './features/odds/oddsSlice';
import bettingScoresReducer from './features/bettingScores/bettingScoresSlice';

export const store = configureStore({
  reducer: {
    odds: oddsReducer,
    bettingScores: bettingScoresReducer,
  },
});
