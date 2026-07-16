"""Configuration loading with validation."""

import yaml
from pathlib import Path
from typing import Dict, Any, List, Optional


class ConfigValidationError(Exception):
    """Raised when configuration is invalid."""
    pass


def load_config(path: str | Path) -> Dict[str, Any]:
    """Load YAML configuration."""
    path = Path(path)
    
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def validate_config(config: Dict[str, Any]) -> None:
    """Validate required fields exist."""
    required = {
        'project': ['name'],
        'data': ['dataset', 'cancer', 'modalities'],
        'model': ['architecture', 'latent_dim'],
        'training': ['epochs', 'batch_size', 'learning_rate', 'optimizer'],
    }
    
    for section, keys in required.items():
        if section not in config:
            raise ConfigValidationError(f"Missing section: {section}")
        
        for key in keys:
            if key not in config[section]:
                raise ConfigValidationError(
                    f"Missing {section}.{key} in config"
                )


def merge_configs(base: Dict, override: Dict) -> Dict:
    """Deep merge two configs."""
    result = base.copy()
    
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    
    return result


def load_experiment_config(cancer_type: str) -> Dict[str, Any]:
    """Load configuration for a specific cancer type."""
    config_dir = Path(__file__).parent.parent.parent.parent / 'configs'
    
    # Load default
    default_path = config_dir / 'default.yaml'
    if not default_path.exists():
        raise FileNotFoundError("default.yaml not found in configs/")
    
    default_config = load_config(default_path)
    
    # Load cancer-specific
    cancer_path = config_dir / f'{cancer_type.lower()}.yaml'
    if not cancer_path.exists():
        raise FileNotFoundError(
            f"Config for {cancer_type} not found. "
            f"Please create configs/{cancer_type.lower()}.yaml"
        )
    
    cancer_config = load_config(cancer_path)
    
    # Merge
    config = merge_configs(default_config, cancer_config)
    
    # Validate merged config
    validate_config(config)
    
    return config
