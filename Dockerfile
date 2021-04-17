FROM python:alpine3.7
COPY Project_Demo.py /app
COPY requirements.txt /app
EXPOSE 9090
ENTRYPOINT [ "python" ]
CMD [ "Project_Demo.py" ]
