import paramiko
import pytest
from datetime import datetime

def create_and_write_file(test_name, data):
    # get current date and time
    current_datetime = datetime.now()
    file = open(test_name+'__'+str(datetime.timestamp(current_datetime))+'.txt', 'w')
    file.write(data)

def test_1(set_connection):
    """
    Test Case to check the Processor Utilization by firing "mpstat" command.
    If the CPU utilization is greater than 90%, test case fails.
    Reverse assert is used in this case. We can find the CPU idle %.
    If CPU idle % is less than 10%, the test case would fail.

    """
    stdin, stdout, stderr = set_connection.exec_command("mpstat")
    a = stdout.read().decode()
    create_and_write_file('test_1', a)
    print(a)
    s = a.split()
    flag = True
    if float(s[-1]) <= 10:
        flag = False
    assert flag, True


@pytest.mark.cli
def test_3(set_connection):
    """
    Test Case to check the Disk Utilization by firing "df -h" command.
    If the disk utilization is greater than 90%, test case fails.

    """
    stdin, stdout, stderr = set_connection.exec_command("df -h")
    flag, list_output = True, []
    a = stdout.read().decode()
    x = a.split('\n')
    x.pop(len(x)-1)
    for element in x:
        y = element.split()
        if element != x[0]:
            list_output.append(y)

    for element in list_output:
        if float(element[4][:-1]) > 10:
            flag = False
            break

    assert flag, True
