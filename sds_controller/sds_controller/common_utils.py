import redis
import os

from django.conf import settings
from exceptions import FileSynchronizationException


def get_redis_connection():
    return redis.Redis(connection_pool=settings.REDIS_CON_POOL)


def rsync_dir_with_nodes(directory):
    # retrieve nodes
    nodes = get_all_registered_nodes()
    for node in nodes:
        data = {'directory':  directory, 'node_ip': node['ip'], 'ssh_username': node['ssh_username'], 'ssh_password': node['ssh_password']}
        rsync_command = 'sshpass -p {ssh_password} rsync --progress -avrz -e ssh {ssh_username}@{node_ip}:{directory} {directory}'.format(**data)
        # print "System: %s" % rsync_command
        ret = os.system(rsync_command)
        if ret != 0:
            raise FileSynchronizationException("An error occurred copying files to Swift nodes")


def get_all_registered_nodes():
    """
    Returns all registered nodes
    :return:
    """
    r = get_redis_connection()
    keys = r.keys("node:*")
    nodes = []
    for key in keys:
        node = r.hgetall(key)
        nodes.append(node)
    return nodes
