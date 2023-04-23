FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN apt-get update && apt-get install -y iputils-ping

# 
COPY /Code /code
# 
CMD ["uvicorn", "RouterApp:app", "--host", "0.0.0.0", "--port", "80"]
