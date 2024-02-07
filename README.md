# Stationery Shop API
This is a simple API for a stationery shop. It is built using Flask and SQLAlchemy. It is a RESTful API that allows you to perform CRUD operations on the database.

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
