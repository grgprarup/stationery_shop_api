#!/bin/bash
conda run -n stationery_shop_api gunicorn --bind 0.0.0.0:5000 "app:create_app()"