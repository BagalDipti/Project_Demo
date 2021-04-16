FROM python:alpine3.7
COPY Project_Demo.py /app
workdir /app
EXPOSE 8080
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "Project_Demo.py" ]
