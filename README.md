# Sales Prediction API

## Overview

The Sales Prediction API is a Flask web application that provides a RESTful API for predicting sales based on various features. This project uses a pre-trained Random Forest model to generate predictions based on input data provided in JSON format.

## Features

- Predicts sales based on input features such as:
  - Competition Distance
  - Is Holiday
  - Store Type
  - Assortment Type
  - Day of Week
  - And more...

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Virtual Environment (optional but recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone <https://github.com/Recklesssss/challenge-4>
   cd <challenge-4>
2. use this to access the predicted sales data in flask usinfg the command line Invoke-RestMethod -Uri http://127.0.0.1:5000/predict -Method POST -Headers @{"Content-Type" = "application/json"} -Body '{"CompetitionDistance": 1000, "Promo": 1, "DayOfWeek": 3, "Year": 2024, "Month": 9, "StoreType": 1, "Assortment": 1, "Store": 1, "CompetitionOpenSinceMonth": 5, "CompetitionOpenSinceYear": 2010, "Promo2": 0, "Promo2SinceWeek": 12, "Promo2SinceYear": 2012, "PromoInterval": 1, "HolidayFlag": 0, "SchoolHoliday": 1, "StateHoliday": 0, "IsWeekend": 0, "Day": 15, "WeekOfYear": 38, "Customers": 100, "StoreOpen": 1, "IsHoliday": 0, "Sales": 1200}'
>>