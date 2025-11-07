import pytest
from unittest.mock import patch

@pytest.fixture(autouse=True)
def mock_vault():
    with patch("core.vault.Vault", autospec=True) as MockVault:
        instance = MockVault.return_value
        instance.get_key.return_value = "mocked-secret"
        yield

@pytest.fixture(autouse=True)
def mock_vault_decrypt():
    with patch("core.vault_encryption.vault_decrypt", return_value="decrypted-value"):
        yield
