import mock


mocked_method = mock.Mock(side_effect=[1, 2, 3])
print('Call(1): ', mocked_method('A'))
print('Call(2): ', mocked_method('B'))
print('Call(3): ', mocked_method('C'))

mocked_method.assert_has_calls([
    mock.call('A'),
    mock.call('B'),
    mock.call('C'),
])

print('Call(4): ', mocked_method())
