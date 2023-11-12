# infra-test
<h3>How does Kubernetes work, and when we need to have Kubernetes?</h3>
Kubernetes manages and helps orchestrates workflows. It mainly operates through a system of containers, pods, nodes, and
a master. Pods house containers that share resources and network, and can communicate through localhost. Nodes run pods
and contain a kubelet which can communicate with the master. Each master in turn manages a cluster, and has functions
such as a scheduler.
Kubernetes brings containerized apps more stability, via automatically provisioning resources based on the amount of traffic, 
as well as being able to monitor containers and 
nodes (replace and restart). This is especially valuable for when there is a need for scale in order to handle increased
load, as well as efficiently manage resources.
<h3>How to control behavior from developer / engineer related to access control and usage control?</h3>
We can utilize modules such as AWS Identity and Access Management to implement role based access control in order to 
restrict who can view each module, as well as enforce authentication for each user to access a specific module.
In addition, applying access logging is also crucial to stop unauthorized access of sensitive information. To control
usage, training can be implemented to stop users from indulging in risky activities such as clicking on fishy links,
hard coding credentials, pasting sensitive code in websites, or opening attachments. Furthermore, we can implement a 
NIST framework to be fully prepared should any incidents arise.
<br>
Quickstart
<br>
Install Dependencies
<pre>
  pip install requirements.txt
  brew install rabbitmq
  brew install prometheus
  brew install grafana
  brew info rabbitmq 
  rabbitmq-plugins enable rabbitmq_prometheus
  CONF_ENV_FILE="/opt/homebrew/etc/rabbitmq/rabbitmq-env.conf" /opt/homebrew/opt/rabbitmq/sbin/rabbitmq-server
  brew services start prometheus
  brew services start grafana
  cd src
  python main.py
</pre>
In prometheus yml file add
<pre>
  - job_name: 'rabbitmq'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:15692']
        labels:
          group: 'production'
</pre>
Run consumer to see consumer logs
<pre>
  python queue/consumer.py
</pre>
Afterwards, you can integrate grafana and prometheus data.