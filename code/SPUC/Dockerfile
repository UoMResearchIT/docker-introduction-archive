FROM python:3.12-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./*.py /code/
RUN mkdir /code/output

ENTRYPOINT ["python", "/code/spuc.py"]
CMD ["--units", "iuhc"]
