# 🚀 Can My CubeSat Survive?

A Flask-based CubeSat mission survival simulator that predicts whether a CubeSat can complete a 30-day mission based on its power budget.

---

## Project Overview

CubeSats are small satellites with limited power resources. A mission can fail if the satellite consumes more energy than it generates.

This project simulates a simplified 30-day CubeSat mission and determines whether the spacecraft survives based on:

* Orbit Altitude
* Battery Capacity
* Solar Panel Area
* Payload Power Consumption

The simulator tracks battery levels day by day and reports mission success or failure.

---

## Why I Built This

I built this project to learn:

* Python
* Flask
* HTML/CSS
* JavaScript
* Data visualization using Chart.js
* Basic spacecraft power-budget concepts

The goal was to create a complete engineering-style simulator rather than a simple calculator.

---

## Features

* 30-day mission simulation
* Day-by-day power budget calculation
* Battery tracking throughout the mission
* Mission survival/failure prediction
* Failure day and failure reason reporting
* Interactive battery-level graph
* Detailed mission log table
* Input validation and error handling

---

## Technology Stack

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Visualization

* Chart.js

---

## Simplified Simulation Model

This project uses a simplified power-budget model designed for learning purposes.

### Power Generation

Power generated each day:

Solar Generation = Solar Panel Area × 0.02 × 24 × Altitude Factor

Where:

* Solar Panel Area is entered in cm²
* Altitude Factor varies with orbit altitude
* The altitude factor is limited between 0.8 and 1.2

### Power Consumption

Daily power consumption:

Power Consumption = (Payload Power + 1) × 24

The additional 1 W represents simplified spacecraft housekeeping power.

### Mission Failure Condition

A mission fails when:

Battery Remaining ≤ 0 Wh

The simulator reports:

* Failure Day
* Failure Reason

---

## Project Structure

can-my-cubesat-survive/

├── app.py

├── requirements.txt

├── README.md

├── simulator/

│   └── power_model.py

├── templates/

│   ├── index.html

│   └── result.html

├── static/

│   └── style.css

└── venv/

---

## How to Run Locally

### 1. Clone the Repository

git clone <repository-url>

cd can-my-cubesat-survive

### 2. Create a Virtual Environment

python -m venv venv

### 3. Activate the Virtual Environment

Windows:

venv\Scripts\activate

### 4. Install Dependencies

pip install -r requirements.txt

### 5. Run the Application

python app.py

### 6. Open in Browser

http://127.0.0.1:5000

---

## Example Inputs

Orbit Altitude: 500 km

Battery Capacity: 1000 Wh

Solar Panel Area: 200 cm²

Payload Power Draw: 2 W

---

## Output

The simulator generates:

* Mission Status (Survived / Failed)
* Failure Day (if applicable)
* Failure Reason
* Battery-Level Graph
* Daily Mission Log

---

## Future Improvements (Version 2)

Possible enhancements include:

* Eclipse modelling
* Battery degradation
* Adjustable mission duration
* Multiple payload modes
* Solar panel efficiency settings
* Downloadable mission reports
* More realistic orbital power calculations

---

## Disclaimer

This project is an educational simulator and does not use real orbital mechanics or flight-qualified spacecraft power models.

The calculations are intentionally simplified for learning and demonstration purposes.
