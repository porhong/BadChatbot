FROM python:3.9.18-slim
ADD main_1.2.0.py .
ADD .env .
RUN apt update
RUN pip 
RUN pip install --upgrade openai
RUN pip install aiogram==2.25.2
RUN pip install requests
RUN pip install python-dotenv
CMD [ "python3","./gpt.py" ]
