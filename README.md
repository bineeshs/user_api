# user_api

This project implements a Django REST Framework (DRF) API endpoint for processing user data from an uploaded CSV file. The API validates the data, saves valid records into a database, and provides detailed feedback for rejected records.

---

## Features

- Accepts only `.csv` files for upload.
- Validates CSV data with the following rules:
  - `name`: Must be a non-empty string.
  - `email`: Must be a valid email address.
  - `age`: Must be an integer between 0 and 120.
- Skips duplicate email addresses gracefully.
- Returns a summary of successfully saved records, rejected records, and detailed validation errors.

---

## Requirements

- Python 3.8+
- Django 4.0+
- Django REST Framework (DRF) 3.12+

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
