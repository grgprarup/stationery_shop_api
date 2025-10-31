# Stationery Shop API
The Stationery Shop API is a simple yet powerful backend service built using Flask and SQLAlchemy. It provides a clean and efficient way to manage stationery inventory data through standard CRUD operations.

⚙️ Key Features

* 🗂 Create, Read, Update, Delete (CRUD) — Manage inventory records seamlessly.

* 🧱 Flask + SQLAlchemy Stack — Combines the simplicity of Flask with the robustness of SQLAlchemy ORM.

* 🔗 RESTful Architecture — Ensures structured, scalable, and maintainable API design.

* 💾 Database Integration — Store and retrieve inventory data efficiently with relational database support.

## Prerequisites
- [Python](https://www.python.org/) 3.11 or higher
- [Conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) 23.7.4 or higher

## Installation
1. Clone the repository
   ```
   git clone https://github.com/grgprarup/stationery_shop_api.git
   cd stationery_shop_api
   ```
2. Create a virtual environment using conda
   ```
   conda create -n stationery_shop_api
   ```
   OR using environment.yml
   ```
   conda env create -f environment.yml
   ```
3. Activate and Deactivate the virtual environment
   ```
   conda activate stationery_shop_api
   ```
   ```
   conda deactivate
   ```
4. Install or Update the dependencies
   ```
   conda env update -f environment.yml
   ```
5. Run the app
   ```
   flask run
   ```

## Run the app using Docker
1. Build the Docker image
   ```
   docker build -t stationery_shop_api .
   ```
2. Run the Docker container
   ```
   docker run -d -p 5000:5000 stationery_shop_api
   ```

### Create environment.yml
```
conda env export > environment.yml
```

### Delete environment
```
conda env remove -n stationery_shop_api
```

## Usage
The API is hosted on http://127.0.0.1:5000.
