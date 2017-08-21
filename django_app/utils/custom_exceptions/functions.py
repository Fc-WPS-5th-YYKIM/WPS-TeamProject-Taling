from utils.custom_exceptions.exceptions import CustomIndexError

__all__ = (
    'custom_index_error',
)


def custom_index_error(validated_data, key, length):
    if len(validated_data[key]) == length:
        return validated_data[key]
    else:
        raise CustomIndexError(key)
