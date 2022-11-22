FROM python:3
ADD QRProg.py /
RUN apt-get update && apt-get install flask && apt-get install pystrich
ENTRYPOINT nano QRProg.py && export FLASK_APP=generate_qrcode && export FLASK_ENV=development && flask run
