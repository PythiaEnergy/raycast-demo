# raycast-demo

This repository provides example code for getting requests from  API V2. 

## Repository Contents

* `demo.ipynb`: A Jupyter Notebook for querying and visualizing weather data from a weather forecasting API.
* `.env`: A file for securely storing credentials (USERNAME and PASSWORD).
* `requirements.txt`: Lists all required dependencies for the project.
* `auth.py`: Handles Firebase authentication for secure user login and access.
* `data/stations_knmi.py`: Contains the locations and metadata of KNMI weather stations in the Netherlands.

## Installation:

**1. Clone the repository**
```bash
git clone https://github.com/PythiaEnergy/raycast-demo.git
cd raycast-demo
```

**2. Install Dependencies:**

```bash
pip install -r requirements.txt
```

**3. Create a `.env` File:** Create a .env file in the root directory and add your credentials:

```bash
USERNAME=your_username
PASSWORD=your_password
```

## Data


`data/stations_knmi.csv`
* Contains KNMI station locations, including station IDs, names, and coordinates.

## Contact

For further questions or feedback, reach out to info@pythia-energy.nl.
