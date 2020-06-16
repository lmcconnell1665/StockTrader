import boto3

def main():

    dynamodb = boto3.resource('dynamodb', 'us-east-1')
    table = dynamodb.Table('WeeklyStock')
            
if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    main()