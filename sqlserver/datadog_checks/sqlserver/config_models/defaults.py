# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>


def instance_adoprovider():
    return 'SQLOLEDB'


def instance_autodiscovery_db_service_check():
    return True


def instance_command_timeout():
    return 10


def instance_connector():
    return 'adodbapi'


def instance_database():
    return 'master'


def instance_database_autodiscovery():
    return False


def instance_database_autodiscovery_interval():
    return 3600


def instance_database_instance_collection_interval():
    return False


def instance_dbm():
    return False


def instance_disable_generic_tags():
    return False


def instance_driver():
    return 'SQL Server'


def instance_empty_default_hostname():
    return False


def instance_ignore_missing_database():
    return False


def instance_include_ao_metrics():
    return False


def instance_include_db_fragmentation_metrics():
    return False


def instance_include_fci_metrics():
    return False


def instance_include_instance_metrics():
    return True


def instance_include_master_files_metrics():
    return False


def instance_include_task_scheduler_metrics():
    return False


def instance_log_unobfuscated_plans():
    return False


def instance_log_unobfuscated_queries():
    return False


def instance_min_collection_interval():
    return 15


def instance_only_custom_queries():
    return False


def instance_only_emit_local():
    return False


def instance_proc_only_if_database():
    return 'master'


def instance_server_version():
    return '2014'


def instance_use_global_custom_queries():
    return 'true'
