FROM python:alpine3.7
COPY Project_Demo.py /app
COPY requirements.txt /app
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "Project_Demo.py" ]
