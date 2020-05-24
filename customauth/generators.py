from oauthlib.common import UNICODE_ASCII_CHARACTER_SET
from oauthlib.common import generate_client_id as oauthlib_generate_client_id


class BaseHashGenerator(object):
    """
    All generators should extend this class overriding `.hash()` method.
    """

    def hash(self):
        raise NotImplementedError()


class ClientIdGenerator(BaseHashGenerator):
    """Generate a client_id for Basic Authentication scheme without colon char
        as in http://tools.ietf.org/html/rfc2617#section-2
        """

    def hash(self):
        length = 40
        chars = UNICODE_ASCII_CHARACTER_SET
        return oauthlib_generate_client_id(length=length, chars=chars)


class ClientSecretGenerator(BaseHashGenerator):
    """ Generate a client_id for Basic Authentication scheme without colon char
        as in http://tools.ietf.org/html/rfc2617#section-2"""

    def hash(self):
        length = 40
        chars = UNICODE_ASCII_CHARACTER_SET
        return oauthlib_generate_client_id(length=length, chars=chars)


def generate_client_id():
    """
    Generate a suitable client id
    """
    client_id_generator = ClientIdGenerator()
    return client_id_generator.hash()


def generate_client_secret():
    """
    Generate a suitable client secret
    """
    client_secret_generator = ClientSecretGenerator()
    return client_secret_generator.hash()
