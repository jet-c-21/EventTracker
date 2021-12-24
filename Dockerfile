FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV w_dir=EventTracker
WORKDIR /${w_dir}
COPY requirements.txt /${w_dir}/
RUN apt-get update \
    &&  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata

RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

RUN apt-get install cron -y
RUN pip install --user --upgrade pip
RUN pip install -r requirements.txt
COPY . /${w_dir}/