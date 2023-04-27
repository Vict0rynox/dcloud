FROM lscr.io/linuxserver/openssh-server:latest

EXPOSE 8080

RUN apk add --no-cache vim curl

RUN sed -i 's/GatewayPorts no/GatewayPorts yes/' /etc/ssh/sshd_config
RUN sed -i 's/AllowTcpForwarding no/AllowTcpForwarding yes/' /etc/ssh/sshd_config

RUN echo 'GatewayPorts yes' >> /etc/ssh/sshd_config && \
    echo 'AllowTcpForwarding yes' >> /etc/ssh/sshd_config && \
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
