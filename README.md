# 🚀 Can My CubeSat Survive?

A Flask-based CubeSat mission survival simulator that predicts whether a CubeSat can complete a 30-day mission based on its power budget.

---

## Live Demo

https://devamayookha.pythonanywhere.com

---

## Project Overview

CubeSats are small satellites with strict power constraints. A mission can fail if the spacecraft consumes energy faster than it generates it.

This project simulates a simplified 30-day CubeSat mission and determines whether the satellite survives based on:

* Orbit Altitude
* Battery Capacity
* Solar Panel Area
* Payload Power Draw

The simulator tracks battery levels day-by-day and reports mission success or failure.

---

## Why I Built This

I built this project to learn:

* Python programming
* Flask web development
* HTML and CSS
* JavaScript fundamentals
* Data visualization with Chart.js
* Basic spacecraft power-budget concepts

The goal was to create a complete engineering-style simulation project from scratch and deploy it publicly.

---

## Features

✅ 30-day mission simulation

✅ Day-by-day power budget calculation

✅ Battery level tracking

✅ Mission survival/failure prediction

✅ Failure day reporting

✅ Failure reason reporting

✅ Interactive battery-level graph

✅ Detailed mission log table

✅ Input validation and error handling

✅ Public deployment

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

### Deployment

* PythonAnywhere

---

## How the Simulation Works

This project uses a simplified power-budget model designed for learning and demonstration purposes.

### Step 1: Solar Power Generation

Daily power generation is estimated using:

Solar Generation = Solar Panel Area × 0.02 × 24 × Altitude Factor

Where:

* Solar Panel Area is entered in cm²
* Altitude Factor changes with orbit altitude
* Altitude Factor is limited between 0.8 and 1.2

### Step 2: Power Consumption

Daily power consumption is estimated using:

Power Consumption = (Payload Power + 1) × 24

The additional 1 W represents simplified spacecraft housekeeping power.

### Step 3: Battery Update

Battery Remaining = Previous Battery + Generated Power − Consumed Power

### Step 4: Mission Outcome

The mission fails when:

Battery Remaining ≤ 0 Wh

The simulator reports:

* Failure Day
* Failure Reason

Otherwise, the CubeSat successfully completes the full 30-day mission.

---

## Project Structure

```text
can-my-cubesat-survive/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── simulator/
│   └── power_model.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── venv/
```

## Installation and Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/devamayookha/can-my-cubesat-survive.git
cd can-my-cubesat-survive
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open in Browser

```text
http://127.0.0.1:5000
```

---

## Example Mission

Input:

* Orbit Altitude: 500 km
* Battery Capacity: 1000 Wh
* Solar Panel Area: 200 cm²
* Payload Power Draw: 2 W

Output:

* Mission Status
* Battery-Level Graph
* Daily Mission Log
* Failure Details (if applicable)

---

## Screenshot

After running a simulation, the application displays:

* Mission status card
* Battery trend graph
* Day-by-day mission log
* Final battery status

## Screenshot

Screenshots will be added in future updates.

---

## Future Improvements (Version 2)

Potential future enhancements:

* Eclipse modelling
* Battery degradation
* Adjustable mission duration
* Multiple payload operating modes
* Solar panel efficiency settings
* Downloadable mission reports
* CSV export
* More realistic orbital power calculations
* Environmental effects on power generation

---

## Disclaimer

This project is an educational simulator.

It does not use real orbital mechanics, spacecraft flight software, or professional mission-analysis tools. The calculations are intentionally simplified to support learning, experimentation, and demonstration of software development concepts.

---

## Author

**B. R. Devamayookha**

B.Tech Artificial Intelligence & Data Science

Sona College of Technology

GitHub: https://github.com/devamayookha
