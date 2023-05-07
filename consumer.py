import pika, os, time
CLOUD_AMQP = ''

def process_function(msg):
  print(" Msg processing ...")
  print(" [x] Received " + str(msg))

  #time.sleep(5) # delays for 5 seconds
  print(" PDF processing finished");
  return;

url = os.environ.get('CLOUDAMQP_URL', f'{CLOUD_AMQP}')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='MyQueue1')

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  process_function(body)

# set up subscription on the queue
channel.basic_consume('MyQueue1', callback, auto_ack=True)

channel.start_consuming()
connection.close()
