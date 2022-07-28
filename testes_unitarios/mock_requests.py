@patch('requests.post')
@mock.patch.dict(os.environ, {'URL': 'htthp://www.url.com'})
def test_token_200(self, mocked_post):
    mocked_post.return_value = Mock(
        status_code=200, json=lambda: {"acess_token": "T0K3N"})
    crendentials = {'client_id': 'UnitTest', 'client_secret': 'UnitTest'}
    key.get_token(crendentials)
    self.assertEqual('TOKEN_TESTE', key.token)
