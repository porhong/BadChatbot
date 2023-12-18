FROM python:3.11.5-slim
ADD main_1.3.0_gemini.py .
ADD .env .
RUN apt update
RUN pip install -U google-generativeai
RUN pip install aiogram==2.25.2
RUN pip install python-dotenv
RUN pip install Pillow
CMD [ "python3","./main_1.3.0_gemini.py" ]
