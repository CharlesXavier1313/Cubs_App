import React, { useEffect, useState } from 'react';
import { Pie } from 'react-chartjs-2';
import axios from 'axios';

const WinLossChart = () => {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('/api/win_loss_data');
        const { wins, losses } = response.data;
        
        setChartData({
          labels: ['Wins', 'Losses'],
          datasets: [
            {
              data: [wins, losses],
              backgroundColor: ['#4CAF50', '#F44336'],
              hoverBackgroundColor: ['#45a049', '#e53935']
            }
          ]
        });
      } catch (error) {
        console.error('Error fetching win-loss data:', error);
      }
    };

    fetchData();
  }, []);

  if (!chartData) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Cubs Win-Loss Record</h2>
      <Pie data={chartData} />
    </div>
  );
};

export default WinLossChart;