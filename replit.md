# Telegram Bot Backend - Replit Setup

## Overview
This is a Python-based Telegram bot backend application that connects to a PostgreSQL database (Neon.tech). The application provides database management utilities and is designed to handle inventory data for stores/shops.

## Current State
- **Status**: Successfully configured and running on Replit
- **Language**: Python 3.11
- **Database**: PostgreSQL (Neon.tech)
- **Main Purpose**: Telegram bot backend for inventory management

## Recent Changes (October 7, 2025)
- Initial Replit environment setup completed
- Installed Python 3.11 and all required dependencies
- Configured environment secrets (DATABASE_URL, TELEGRAM_BOT_TOKEN)
- Created workflow to run the bot backend
- Verified successful database connection
- Application tested and working correctly

## Project Architecture

### File Structure
```
├── main.py                 # Main application entry point
├── utils/
│   └── db_manager.py      # Database connection and query utilities
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore file
└── replit.md              # This documentation file
```

### Key Components

#### 1. Database Manager (`utils/db_manager.py`)
- Handles PostgreSQL connection using psycopg2
- Functions:
  - `setup_database()`: Verifies database connection
  - `execute_query()`: Executes SQL queries with parameter support
  - `fetch_data()`: Retrieves data from database
  - `insert_update_data()`: Modifies database records
  - `create_initial_tables()`: Creates initial database schema

#### 2. Database Schema
- `tiendas_suscriptores`: Stores store/subscriber information
  - telegram_id (PRIMARY KEY)
  - tienda_nombre
  - fecha_vencimiento
  - es_admin
- `datos_inventario`: Stores inventory data
  - id (SERIAL PRIMARY KEY)
  - telegram_id (FOREIGN KEY)
  - producto_nombre
  - cantidad
  - fecha_registro

#### 3. Main Application (`main.py`)
- Loads environment variables using python-dotenv
- Verifies database connection on startup
- Debug output for environment variable verification

### Dependencies
- `python-telegram-bot`: Telegram bot API library
- `psycopg2-binary`: PostgreSQL database adapter
- `python-dotenv`: Environment variable management

### Environment Variables
- `DATABASE_URL`: PostgreSQL connection string (configured)
- `TELEGRAM_BOT_TOKEN`: Telegram bot authentication token (configured)

### Workflow
- **Name**: Bot Backend
- **Command**: `python main.py`
- **Output Type**: Console
- **Status**: Running successfully

## Next Steps (Future Development)
The current setup includes database connectivity verification. Future development might include:
- Implementing Telegram bot commands and handlers
- Adding CRUD operations for inventory management
- User authentication and authorization
- Admin panel features
- Subscription management

## Notes
- All environment secrets are properly configured via Replit Secrets
- Database connection is verified and working
- The application uses Neon.tech for PostgreSQL hosting
- Code includes Spanish language comments (original codebase)
