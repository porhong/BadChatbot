FROM python:3.9
ADD main.py .
RUN pip install aiogram==2.25.2
RUN pip install google-generativeai
CMD [ "python","./main.py" ]
