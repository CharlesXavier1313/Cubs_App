# Cubs Betting Analytics Web App

## Overview

This web application provides advanced analytics and predictions for Cubs betting. It leverages historical data, player statistics, and real-time odds to offer insights for Moneyline, Over/Under, and Run Line bets.

## Features

- **Data Collection**: Gathers Cubs players and game statistics, as well as Vegas odds data from various sources.
- **Data Analysis**: Performs exploratory data analysis and feature engineering to identify key betting indicators.
- **Model Development**: Utilizes machine learning models for Moneyline, Over/Under, and Run Line bet predictions.
- **API**: Provides RESTful endpoints for retrieving odds, betting scores, historical data, and custom analysis.
- **Frontend**: Interactive React-based UI for displaying odds, betting scores, historical data, and visualizations.
- **Monitoring**: Implements Prometheus and Grafana for real-time performance monitoring and alerting.
- **Logging**: Aggregates logs using the ELK (Elasticsearch, Logstash, Kibana) stack for comprehensive system insights.
- **Backups**: Automated backup system for PostgreSQL and Elasticsearch data to ensure data integrity and disaster recovery.
- **Control Panel**: A user-friendly interface to start and stop the application with a single click.

## Architecture

The application follows a microservices architecture:

- **Backend**: FastAPI-based RESTful API
- **Frontend**: React single-page application
- **Database**: PostgreSQL for structured data storage
- **Cache**: Redis for high-performance data caching
- **Message Queue**: RabbitMQ for asynchronous task processing
- **Monitoring**: Prometheus and Grafana
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)

## Installation

### Prerequisites

- Docker (version 20.10 or later)
- Docker Compose (version 1.29 or later)
- Git

### Steps

1. Clone the repository:
   ```
   git clone https://github.com/your-username/cubs_betting.git
   cd cubs_betting
   ```

2. Build and start the application:
   ```
   ./deploy_all.sh
   ```

   This script builds the Docker images and starts all necessary services.

## Usage

1. Access the web application:
   ```
   http://localhost:5000
   ```

2. Use the Control Panel to manage the application:
   - Navigate to the "Control Panel" section in the application.
   - Click the "Start App" button to initiate the application.
   - Click the "Stop App" button to halt the application.

3. Navigate through different sections to view odds, betting scores, and historical data.

## API Endpoints

- `/api/games`: Retrieve game data
- `/api/odds`: Get current odds for upcoming games
- `/api/betting_scores`: Retrieve betting scores based on our models
- `/api/win_loss_data`: Get win-loss statistics
- `/api/betting_stats`: Retrieve overall betting statistics
- `/api/start`: Start the application (used by the Control Panel)
- `/api/stop`: Stop the application (used by the Control Panel)

For a complete API documentation, visit `/docs` when the application is running.

## Development

### Backend (FastAPI)

1. Navigate to the `src` directory
2. Make changes to the relevant files
3. Rebuild and restart the backend:
   ```
   docker-compose up -d --build backend
   ```

### Frontend (React)

1. Navigate to the `frontend/src` directory
2. Make changes to the relevant components or features
3. Rebuild and restart the frontend:
   ```
   docker-compose up -d --build frontend
   ```

### Database

1. Edit the `models.py` file for schema changes
2. Apply migrations:
   ```
   docker-compose run backend alembic upgrade head
   ```

## Monitoring and Logging

- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:5000`
- Kibana: `http://localhost:5601`

## Backups

Automated backups are configured for PostgreSQL and Elasticsearch. Backup scripts are located in the `scripts` directory.

## Testing

Run the test suite:
```
docker-compose run backend pytest
```

## Deployment

For production deployment:

1. Update environment variables in `docker-compose.prod.yml`
2. Build and deploy:
   ```
   docker-compose -f docker-compose.prod.yml up -d
   ```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) for details.

## Acknowledgments

- Chicago Cubs organization
- MLB for providing historical data
- All contributors and users of this application

## Support

For support, please open an issue in the GitHub repository or contact the maintainers directly.