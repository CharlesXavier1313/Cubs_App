import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

export const fetchBettingScores = createAsyncThunk('bettingScores/fetchBettingScores', async (gameId) => {
  const response = await axios.get(`http://localhost:8000/api/v1/betting-scores/${gameId}`);
  return response.data;
});

const bettingScoresSlice = createSlice({
  name: 'bettingScores',
  initialState: {
    score: null,
    status: 'idle',
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchBettingScores.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchBettingScores.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.score = action.payload.score;
      })
      .addCase(fetchBettingScores.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      });
  },
});

export default bettingScoresSlice.reducer;
