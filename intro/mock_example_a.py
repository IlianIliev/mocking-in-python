import mock


mocked_method = mock.Mock(return_value='return value')
print('Call: ', mocked_method(123))
mocked_method.assert_called_once_with(123)
