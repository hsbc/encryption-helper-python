import os

import pytest

pytest.importorskip("cryptography.hazmat.primitives.asymmetric.mldsa")

from cryptography.hazmat.primitives import serialization
from encryption_helper.main import generate_mldsa_key, generate_mlkem_key


def _generate_or_skip(generate):
    try:
        return generate()
    except RuntimeError:
        pytest.skip("post quantum algorithms are not available in this backend")


def test_mldsa_generates_pem_keypair(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    public_key, private_key = _generate_or_skip(generate_mldsa_key)
    assert b"BEGIN PUBLIC KEY" in public_key
    assert b"BEGIN PRIVATE KEY" in private_key
    assert (tmp_path / "keys" / "pem" / "mldsa-public-key.pem").exists()
    assert (tmp_path / "keys" / "pem" / "mldsa-private-key.pem").exists()


def test_mldsa_private_key_is_not_printed(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    _, private_key = _generate_or_skip(generate_mldsa_key)
    captured = capsys.readouterr()
    assert private_key.decode() not in captured.out


@pytest.mark.skipif(os.name != "posix", reason="file mode check is posix only")
def test_mldsa_private_key_is_owner_only(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    _generate_or_skip(generate_mldsa_key)
    private_key_path = tmp_path / "keys" / "pem" / "mldsa-private-key.pem"
    mode = os.stat(private_key_path).st_mode & 0o777
    assert mode == 0o600


def test_mldsa_sign_and_verify_roundtrip(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    _generate_or_skip(generate_mldsa_key)
    private_key_path = tmp_path / "keys" / "pem" / "mldsa-private-key.pem"
    private_key = serialization.load_pem_private_key(
        private_key_path.read_bytes(), password=None
    )
    message = b"settlement instruction"
    signature = private_key.sign(message)
    private_key.public_key().verify(signature, message)


def test_mlkem_generates_pem_keypair(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    public_key, private_key = _generate_or_skip(generate_mlkem_key)
    assert b"BEGIN PUBLIC KEY" in public_key
    assert b"BEGIN PRIVATE KEY" in private_key
    assert (tmp_path / "keys" / "pem" / "mlkem-public-key.pem").exists()
    assert (tmp_path / "keys" / "pem" / "mlkem-private-key.pem").exists()


@pytest.mark.skipif(os.name != "posix", reason="file mode check is posix only")
def test_mlkem_private_key_is_owner_only(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    _generate_or_skip(generate_mlkem_key)
    private_key_path = tmp_path / "keys" / "pem" / "mlkem-private-key.pem"
    mode = os.stat(private_key_path).st_mode & 0o777
    assert mode == 0o600
