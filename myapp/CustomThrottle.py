from rest_framework.throttling import UserRateThrottle


class ForGetViewThrottle(UserRateThrottle):
    scope = 'burst'


class ForPostViewThrottle(UserRateThrottle):
    scope = 'postBurst'
