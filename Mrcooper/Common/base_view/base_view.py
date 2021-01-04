from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from Mrcooper.Common.response import ResponseInfo


class BaseView:
    """
    Used for non-authenticated views
    """
    def response(self, token="", status=HTTP_200_OK, is_success=True, data={}, message="", secured=False):
        response = ResponseInfo(token=token, data=data, status=status, isSuccess=is_success,
                                message=message, secured=secured).response
        return Response(response)

    def audit_trail(self, **kwargs):
        pass

    def log(self, **kwargs):
        pass
