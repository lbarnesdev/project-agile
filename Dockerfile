FROM odoo:15

USER root

RUN apt-get update && apt-get upgrade -y
RUN apt-get install git openssh-client -y
RUN mkdir -p /home/odoo \
    && chown odoo:odoo -R /home/odoo

USER odoo