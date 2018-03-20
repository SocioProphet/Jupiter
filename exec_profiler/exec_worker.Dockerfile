FROM ubuntu:16.04

RUN apt-get -yqq update

RUN apt-get -yqq install python3-pip python3-dev libssl-dev libffi-dev
RUN apt-get -yqq update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -yqq install python3-pip python3-dev libssl-dev libffi-dev
RUN apt-get install -yqq openssh-client openssh-server bzip2 wget net-tools sshpass screen
RUN apt-get install -y vim
RUN apt-get install g++ make openmpi-bin libopenmpi-dev -y
RUN apt-get install sudo -y
RUN apt-get install iproute2 -y

RUN apt-get install -y openssh-server
RUN echo 'root:PASSWORD' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

ADD exec_profiler/requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

RUN mkdir -p /home/darpa/apps/data


# IF YOU WANNA DEPLOY A DIFFERENT APPLICATION JUST CHANGE THIS LINE
ADD task_specific_files/network_monitoring_app/scripts/ /centralized_scheduler/
COPY task_specific_files/network_monitoring_app/sample_input /centralized_scheduler/sample_input

ADD task_specific_files/network_monitoring_app/configuration.txt /centralized_scheduler/DAG.txt

ADD exec_profiler/profiler_worker.py /centralized_scheduler/profiler.py

ADD exec_profiler/start_worker.sh /centralized_scheduler/start.sh
ADD exec_profiler/keep_alive.py /centralized_scheduler/keep_alive.py
ADD exec_profiler/get_files.py /centralized_scheduler/get_files.py
ADD jupiter_config.ini /centralized_scheduler/jupiter_config.ini


WORKDIR /centralized_scheduler/

EXPOSE 22 27017 8888

CMD ["./start.sh"]