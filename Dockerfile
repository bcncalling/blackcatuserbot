FROM python:3.8-slim
WORKDIR /blackcatuserbot
COPY . /blackcatuserbot
RUN pip install --no-cache-dir -r requirements.txt
CMD python3 -m bcnplugs
