#!/bin/bash
export PRIVKEYPATH="ssl/privkey.pem";
export CERTFILEPATH="ssl/fullchain.pem";
export BIND_URL="localhost:8001";
export SECRET_WORD="motherland!";
export WORKERS=4;
source ./venv/bin/activate && gunicorn main:app -w $WORKERS -k uvicorn.workers.UvicornWorker -b $BIND_URL --env SECRET_WORD=$SECRET_WORD --log-config logging.conf --keyfile $PRIVKEYPATH --certfile $CERTFILEPATH;