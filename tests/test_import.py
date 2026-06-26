from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def test_app_exists():
    assert (PROJECT_ROOT / "app123.py").exists()


def test_pages_folder_exists():
    assert (PROJECT_ROOT / "pages").exists()


def test_models_folder_exists():
    assert (PROJECT_ROOT / "models").exists()


def test_assets_folder_exists():
    assert (PROJECT_ROOT / "assets").exists()
