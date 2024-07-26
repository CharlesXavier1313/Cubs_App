import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card, Row, Col } from 'react-bootstrap';

const BettingStats = () => {
    const [stats, setStats] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchStats = async () => {
            try {
                const response = await axios.get('/api/betting_stats');
                setStats(response.data);
                setLoading(false);
            } catch (err) {
                setError('Error fetching betting stats');
                setLoading(false);
            }
        };

        fetchStats();
    }, []);

    if (loading) return <div>Loading betting stats...</div>;
    if (error) return <div>{error}</div>;

    return (
        <div>
            <h2>Betting Statistics</h2>
            {stats && (
                <Row>
                    <Col md={4}>
                        <Card>
                            <Card.Body>
                                <Card.Title>Moneyline Win Rate</Card.Title>
                                <Card.Text>{(stats.moneyline_win_rate * 100).toFixed(2)}%</Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col md={4}>
                        <Card>
                            <Card.Body>
                                <Card.Title>Over/Under Win Rate</Card.Title>
                                <Card.Text>{(stats.over_under_win_rate * 100).toFixed(2)}%</Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col md={4}>
                        <Card>
                            <Card.Body>
                                <Card.Title>Run Line Win Rate</Card.Title>
                                <Card.Text>{(stats.run_line_win_rate * 100).toFixed(2)}%</Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            )}
        </div>
    );
};

export default BettingStats;