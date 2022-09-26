# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from datadog_checks.ibm_i.config_models import InstanceConfig
from datadog_checks.ibm_i.config_models.instance import MessageQueueInfo
from datadog_checks.ibm_i.queries import query_map


def test_get_message_queue_info():
    instance_conf_attr = {
        "query_timeout": 1,
        "job_query_timeout": 2,
        "system_mq_query_timeout" : 3,
        "severity_threshold": 50,
    }
    instance_conf = InstanceConfig(
        **instance_conf_attr,
        message_queue_info=MessageQueueInfo(selected_message_queues=[]),
    )
    qmap_output = query_map(instance_conf)
    assert qmap_output['message_queue_info']['name'] == 'message_queue_info'
    assert qmap_output['message_queue_info']['columns'] == [
        {'name': 'message_queue_name', 'type': 'tag'},
        {'name': 'message_queue_library', 'type': 'tag'},
        {'name': 'ibm_i.message_queue.size', 'type': 'gauge'},
        {'name': 'ibm_i.message_queue.critical_size', 'type': 'gauge'},
    ]
    assert qmap_output['message_queue_info']['query']['text'] == (
        'SELECT MESSAGE_QUEUE_NAME, MESSAGE_QUEUE_LIBRARY, COUNT(*), SUM(CASE WHEN SEVERITY >= 50 THEN 1 ELSE 0 END) '  # noqa:E501
        'FROM QSYS2.MESSAGE_QUEUE_INFO GROUP BY MESSAGE_QUEUE_NAME, MESSAGE_QUEUE_LIBRARY'
    )
    assert qmap_output['message_queue_info']['query']['timeout'] == 3
    instance_conf = InstanceConfig(
        **instance_conf_attr,
        message_queue_info=MessageQueueInfo(selected_message_queues=['QSYSOPR']),
    )
    qmap_output = query_map(instance_conf)
    assert qmap_output['message_queue_info']['query']['text'] == (
        'SELECT MESSAGE_QUEUE_NAME, MESSAGE_QUEUE_LIBRARY, COUNT(*), SUM(CASE WHEN SEVERITY >= 20 THEN 1 ELSE 0 END) '
        'FROM QSYS2.MESSAGE_QUEUE_INFO WHERE MESSAGE_QUEUE_NAME IN (\'QSYSOPR\') GROUP BY MESSAGE_QUEUE_NAME, MESSAGE_QUEUE_LIBRARY'  # noqa:E501
    )
    instance_conf = InstanceConfig(
        **instance_conf_attr,
        message_queue_info=MessageQueueInfo(selected_message_queues=['QSYSOPR', 'QPGMR', 'CECUSER']),
    )
    qmap_output = query_map(instance_conf)
    assert qmap_output['message_queue_info']['query']['text'] == (
        'SELECT MESSAGE_QUEUE_NAME, MESSAGE_QUEUE_LIBRARY, COUNT(*), SUM(CASE WHEN SEVERITY >= 30 THEN 1 ELSE 0 END) '
        'FROM QSYS2.MESSAGE_QUEUE_INFO WHERE MESSAGE_QUEUE_NAME IN (\'QSYSOPR\', \'QPGMR\', \'CECUSER\') GROUP BY MESSAGE_QUEUE_NAME, MESSAGE_QUEUE_LIBRARY'  # noqa:E501
    )