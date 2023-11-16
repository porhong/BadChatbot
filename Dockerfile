FROM python:3.11.5-slim
ADD main_1.2.0.py .
ADD .env .
RUN apt update
RUN pip install -U google-generativeai
RUN pip install aiogram==2.25.2
RUN pip install python-dotenv
CMD [ "python3","./main_1.2.0.py" ]
