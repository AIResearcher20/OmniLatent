"""Tests for configuration system."""

import pytest
from omnilatent.utils.config import (
    load_config,
    load_experiment_config,
    merge_configs,
    ConfigValidationError
)


def test_load_brca_config():
    """Test loading BRCA configuration."""
    config = load_experiment_config("BRCA")
    
    assert config["project"]["name"] == "OmniLatent"
    assert config["project"]["cancer_type"] == "BRCA"
    assert config["model"]["latent_dim"] == 128
    assert config["data"]["cancer"] == "BRCA"


def test_config_merge():
    """Test merging defaults with cancer-specific."""
    default = {"model": {"latent_dim": 128, "dropout": 0.2}}
    override = {"model": {"latent_dim": 64}}
    
    merged = merge_configs(default, override)
    assert merged["model"]["latent_dim"] == 64
    assert merged["model"]["dropout"] == 0.2


def test_invalid_config():
    """Test invalid config raises error."""
    with pytest.raises(ConfigValidationError):
        # Missing required field
        invalid = {"project": {"name": "Test"}}  # Missing 'data'
        from omnilatent.utils.config import validate_config
        validate_config(invalid)


def test_missing_cancer():
    """Test missing cancer config raises error."""
    with pytest.raises(FileNotFoundError):
        load_experiment_config("INVALID")
