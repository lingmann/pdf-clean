FROM python:3

RUN pip install pikepdf
ADD pdf-clean.py /

ENTRYPOINT ["/pdf-clean.py"]
