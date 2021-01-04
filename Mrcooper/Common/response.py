class ResponseInfo(object):
    def __init__(self, **args):
        self.response = {
            "token": args.get('token', ""),
            "data": args.get('data', {}),
            "message": args.get('message', ""),
            "status": args.get('status', ""),
            "isSuccess": args.get('isSuccess', True),
            "secured": args.get('secured', False)
        }
