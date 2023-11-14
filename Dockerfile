FROM python:3.9.18-slim
ADD gpt.py .
ADD keep_alive.py .
RUN apt update
RUN pip install --upgrade openai
RUN pip install aiogram==2.25.2
RUN pip install pillow
RUN pip install requests
RUN pip install flask
CMD [ "python3","./gpt.py" ]
