import pytest
import logging
import paramiko


def set_parameters(ipaddress='127.0.0.1', port=2222, username='tanmay', password='tanmay'):
    return ipaddress, port, username, password

@pytest.fixture
def set_connection():
    try:
        # connecting to SSH
        ssh = paramiko.SSHClient()
        # Adding new host key to the local
        # HostKeys object(in case of missing)
        # AutoAddPolicy for missing host key to be set before connection setup.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ip, port_no, user_name, password = set_parameters()
        ssh.connect(ip, port=int(port_no), username=user_name,
                    password=password, timeout=3)
        return ssh

    except Exception as e:
        print("Exception in setting up connection with Virtual Machine. Exception occured is --: \n", str(e))


