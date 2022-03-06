import pika, os, logging
logging.basicConfig()

url = os.environ.get('CLOUDAMQP_URL', 'amqps://qcrhjtsz:4bATF2MDI0JTgtZaGrs6GiRlFoYKcHyd@puffin.rmq2.cloudamqp.com/qcrhjtsz')
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='MyQueue1')

channel.basic_publish(exchange='', routing_key='MyQueue1', body='Tesla is growing 1')
print ("[x] Message sent to consumer")
connection.close()