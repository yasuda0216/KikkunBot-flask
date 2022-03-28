#!/bin/bash
export FLASK_APP=app.py
export FLASK_DEBUG=1
nohup flask run --host='0.0.0.0' --port=5001 >out.log 2>err.log &
