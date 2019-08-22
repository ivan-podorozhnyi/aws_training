from troposphere import Ref
from troposphere.sns import Topic, Subscription


def create_sns(alarm_email):
    email_topic = Topic('email_notification',
                        Subscription=[Subscription(
                            Endpoint=Ref(alarm_email),
                            Protocol="email")])
    return email_topic
