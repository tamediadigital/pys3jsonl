import s3jsonl

bucket = 'tda-kafka'
key = '/logs/2018/09/20/logs-2018-09-20-22-44-1537483472-partition-0.jsonl.gz'
prefix = '/logs/2018/09/20/'

fd = s3jsonl.open_jsonl(bucket, key=key)
len(list(fd))

fd = s3jsonl.open_jsonl(bucket, prefix=prefix)
len(list(fd))
