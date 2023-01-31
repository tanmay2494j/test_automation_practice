import paramiko
import allure
import pytest
from datetime import datetime


def write_data_to_file(test_name, data):
    current_datetime = datetime.now()
    filename = test_name + '.txt'
    with open(filename, 'a+') as file:
        file.write("\n"+str(current_datetime)+"\t:-\n"+data+"\n\n")


def execute_command_and_write_to_file(connection, command, test_name):
    stdin, stdout, stderr = connection.exec_command(command)
    a = stdout.read().decode()
    write_data_to_file(test_name, a)
    return a


def test_1(set_connection):
    """
    Test Case to check the Processor Utilization by firing "mpstat" command.
    If the CPU utilization is greater than 90%, test case fails.
    Reverse assert is used in this case. We can find the CPU idle %.
    If CPU idle % is less than 10%, the test case would fail.
    """
    decoded_output = execute_command_and_write_to_file(connection= set_connection, command='mpstat', test_name='test_1')
    s = decoded_output.split()
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
    decoded_output = execute_command_and_write_to_file(connection= set_connection, command='df -h', test_name='test_3')
    flag, list_output = True, []

    x = decoded_output.split('\n')
    x.pop(len(x)-1)
    for element in x:
        y = element.split()
        if element != x[0]:
            list_output.append(y)

    for element in list_output:
        if float(element[4][:-1]) > 90:
            flag = False
            break
    assert flag, True
