FROM python:3.9-alpine
WORKDIR /usr/share/udemy
ADD conftest.py conftest.py
ADD main.py main.py
ADD test_TestBasicTest.py test_TestBasicTest.py
ADD test_first_example.py test_first_example.py
ADD healthcheck.sh healthcheck.sh
RUN chmod 777 healthcheck.sh

RUN mkdir __logger

# install google chrome

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

# upgrade pip
RUN pip install --upgrade pip

# install selenium
RUN pip install selenium
RUN pip install pytest
#CMD ["pytest"]
ENTRYPOINT sh healthcheck.sh
