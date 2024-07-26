import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

export const fetchOdds = createAsyncThunk('odds/fetchOdds', async (gameId) => {
  const response = await axios.get(`http://localhost:8000/api/v1/odds/${gameId}`);
  return response.data;
});

const oddsSlice = createSlice({
  name: 'odds',
  initialState: {
    odds: [],
    status: 'idle',
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchOdds.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchOdds.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.odds = action.payload;
      })
      .addCase(fetchOdds.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      });
  },
});

export default oddsSlice.reducer;
