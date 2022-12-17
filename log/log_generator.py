import datetime

def log_writer(log_msg):
    with open('log_error.log', mode='a') as l:
        l.write(log_msg)
    l.close()

    return 'Log has been saved!'

def log_error(exception):

    now = datetime.datetime.now()
    
    error_log_msg = f'''
    ====================================================
    An error ocurred while trying execute this code:
    Date and time of error: {now}
    Type of error: {exception}
    ====================================================\n
    '''

    log_writer(log_msg=error_log_msg)

    return error_log_msg