import pytest
import logging
import paramiko


@pytest.fixture
def set_connection():
    try:
        # Create object of SSHClient and
        # connecting to SSH
        ssh = paramiko.SSHClient()

        # Adding new host key to the local
        # HostKeys object(in case of missing)
        # AutoAddPolicy for missing host key to be set before connection setup.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect('127.0.0.1', port=2222, username='tanmay',
                    password='tanmay', timeout=3)
        return ssh

    except Exception as e:
        print("Exception in setting up connection with Virtual Machine. Exception occured is --: \n",str(e))




