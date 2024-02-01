from rest_framework.throttling import UserRateThrottle


class ForGetViewThrottle(UserRateThrottle):
    scope = 'burst'


class ForPostViewThrottle(UserRateThrottle):
    scope = 'postBurst'


class DynamicThrottle(UserRateThrottle):
    def allow_request(self, request, view):
        # Determine the throttle scope based on the request method
        if request.method == 'GET':
            self.scope = 'get_throttle'
        elif request.method == 'POST':
            self.scope = 'post_throttle'

        # Check if the request is allowed based on the determined scope
        return super().allow_request(request, view)