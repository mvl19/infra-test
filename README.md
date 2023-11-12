# infra-test
<h3>How does Kubernetes work, and when we need to have Kubernetes?</h3>
Kubernetes manages and helps orchestrates workflows. Kubernetes brings containerized apps more stability, via 
automatically provisioning resources based on the amount of traffic, as well as being able to monitor containers and 
nodes (replace and restart). This is especially valuable for when you have a service that needs to balance user traffic,
as it may have various downtimes.
<h3>How to control behavior from developer / engineer related to access control and usage control?</h3>
We can utilize modules such as AWS Identity and Access Management 
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