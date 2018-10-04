import boto3
import gzip
import json


def open_jsonl(bucket, key=None, prefix='', suffix='.jsonl.gz'):
    if key is not None:
        if key.startswith('/'):
            key = key[1:]

        yield from _open_jsonl_file(bucket, key)
        return

    for fname in list_jsonl(bucket, prefix, suffix):
        yield from _open_jsonl_file(bucket, fname)


def list_jsonl(bucket, prefix='', suffix='.jsonl.gz'):
    s3 = boto3.client('s3')

    if prefix.startswith('/'):
        prefix = prefix[1:]

    kwargs = {'Bucket': bucket, 'Prefix': prefix}
    while True:
        resp = s3.list_objects_v2(**kwargs)
        for obj in resp['Contents']:
            key = obj['Key']
            if key.endswith(suffix):
                yield key

        try:
            kwargs['ContinuationToken'] = resp['NextContinuationToken']
        except KeyError:
            break


def _open_jsonl_file(bucket, key):
    '''Open a jsonl file or folder (including subfolders) of jsonl files in S3 and return an iterator of records'''

    s3r = boto3.resource('s3')
    fd = s3r.Object(bucket, key).get()['Body']
    fd = gzip.open(fd)

    for line in fd:
        if line.strip():
            yield json.loads(line)
