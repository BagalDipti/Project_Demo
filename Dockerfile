FROM python:3.6
COPY .  /Project_Demo
WORKDIR /Project_Demo
RUN pip install -r requirements.txt
EXPOSE  8000
CMD ["python", "src/Project_Demo.py"]
