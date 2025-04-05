# FROM python:3.11-slim

# WORKDIR /appfastapi

# COPY requirements.txt .

# RUN pip install --upgrade pip && \
#     pip install -r requirements.txt

# COPY . .

# EXPOSE 8000

# ENV PYTHONUNBUFFERED=1 \
#     PYTHONDONTWRITEBYTECODE=1

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# FROM python:3.11-slim

# ENV PYTHONUNBUFFERED=1 \
#     PYTHONDONTWRITEBYTECODE=1

# RUN mkdir -p /home/appfastapi

# WORKDIR /home/appfastapi

# COPY ./blog/requirements.txt /home/appfastapi/requirements.txt

# RUN pip install --upgrade pip && \
#     pip install -r requirements.txt

# COPY ./blog /home/appfastapi

# EXPOSE 8000

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


FROM python:3.9

WORKDIR /code

COPY ./blog/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./blog /code/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]






