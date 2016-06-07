import boto3, json, time
from uuid import uuid4
from creator import create

s3 = boto3.resource('s3')
def upload_s3(source_file, filename):
  bucket_name = '153412-kkanclerz'
  destination_filename = "albums/%s/%s" % (uuid4().hex, filename)
  print destination_filename
  bucket = s3.Bucket(bucket_name)
  bucket.put_object(Key=destination_filename, Body=source_file)

sqs = boto3.resource('sqs')
albumRequests = sqs.get_queue_by_name(QueueName='kanclerj-album')

while True:
  for albumRequest in albumRequests.receive_messages():
    print('processing request ..........')
    albumData = json.loads(albumRequest.body)
    print albumData
    pdf = create(albumData)
    upload_s3(pdf.getvalue(), 'album.pdf')
    albumRequest.delete()
    print('request processing finished [X]')
  time.sleep(1)
