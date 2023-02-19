FROM python:latest

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /code/

RUN ./s.sh

CMD ["streamlit", "run", "streamlit.py"]
