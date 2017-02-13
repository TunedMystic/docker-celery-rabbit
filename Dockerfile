FROM python:3.6-alpine

ENV INSTALL_PATH /worker
ENV INVENTORY_PATH /inventory
RUN mkdir -p $INSTALL_PATH $INVENTORY_PATH

WORKDIR $INSTALL_PATH

COPY ./requirements.txt $INSTALL_PATH
RUN pip install -r requirements.txt

COPY . $INSTALL_PATH
