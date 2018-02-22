# -*- coding: utf-8 -*-

"""

    Module :mod:``


    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
__import__('pkg_resources').declare_namespace(__name__)
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
from core.utils.environ import (
    get_rabbitmq_details,
    get_queue_details
)

from core.mq import SimpleRabbitMQ
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
]


class QueueConsumer(SimpleRabbitMQ):

    def __init__(self, queue_prop, validator=None):

        super(self.__class__, self).__init__(**get_rabbitmq_details())

        self.queue_name, self.queue_durable = queue_prop

        self.validator = validator

        self.callback = None

    def __call__(self, target_func, *args, **kwargs):

        self.callback = target_func

        self.consume(self.queue_name, self.callback)


queues = get_queue_details()

@QueueConsumer(queue_prop=queues['central_logger_queue'])
def logger_queue_consumer(*args, **kwargs):
    print args
    print kwargs


logger_queue_consumer()

