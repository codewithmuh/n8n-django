# Django Ticketing System

A simple Django project with PostgreSQL database for managing customers and tickets.

## Features

- Customer management with phone numbers, names, addresses, and site IDs
- Ticket system with UUID tracking, timestamps, location data, and status management
- Django admin panel for easy data management
- Docker Compose setup for easy deployment

## Quick Start

1. **Build and run the containers:**
   ```bash
   docker-compose up --build
   ```

2. **Access the application:**
   - Django Admin: http://localhost:8000/admin/
   - Login credentials: `admin` / `admin123`

3. **Stop the containers:**
   ```bash
   docker-compose down
   ```

## Database Schema

### Customers Table
- `phone_number` (Primary Key): VARCHAR(20)
- `full_name`: VARCHAR(255) 
- `address`: TEXT
- `site_id`: VARCHAR(100)

### Tickets Table
- `id` (Primary Key): Auto-incrementing integer
- `ticket_uuid`: UUID (auto-generated)
- `reporting_phone`: Foreign key to customers.phone_number
- `ticket_timestamp`: Timestamp with timezone (auto-set)
- `ticket_subject`: Choice field ('self_location', 'registered_address')
- `structured_response`: JSONB field
- `original_free_text`: TEXT
- `openai_summary`: TEXT
- `status`: Choice field ('High Priority', 'Medium Priority', 'Info')
- `location_source`: Choice field ('shared_location', 'from_customers_table')
- `latitude`: Decimal(10,7)
- `longitude`: Decimal(10,7)
- `is_alert_sent`: Boolean (default: False)
- `is_primary_report`: Boolean (default: True)

## Development

The project uses Django 5.0.1 with PostgreSQL 15. All data is persisted in Docker volumes.