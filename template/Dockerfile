FROM python:3.10.10-slim-bullseye

WORKDIR /usr/src
COPY . ./app/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf  ./app/lib \
    && rm -rf  ./app/log \
    && rm -rf  ./app/conf 

ENTRYPOINT ["python", "-OOm", "app"]
CMD [""]
