FROM python:3

ARG DDIR
ARG PORT
ARG IP

ENV DDIR ${DDIR}
ENV PORT ${PORT}
ENV IP ${IP}

WORKDIR ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pandas && \
    pip install --no-cache-dir sqlalchemy && \
    pip install --no-cache-dir psycopg2
COPY add_bd.py ./

CMD python3 add_bd.py --port $PORT --ddir $DDIR --ip $IP