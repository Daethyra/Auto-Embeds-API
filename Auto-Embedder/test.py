
import pytest
import asyncio
import os
from unittest.mock import patch, Mock
from typing import Dict, Union, List
from pinembed import EnvConfig, OpenAIHandler, PineconeHandler, DataStreamHandler

@pytest.fixture
def mock_env_config():
    """Fixture for setting up a mock environment configuration.
    
    Mocks os.getenv to return a test value and initializes EnvConfig.
    
    Returns:
        EnvConfig: Mocked environment configuration
    """
    with patch('os.getenv', return_value="test_value"):
        config = EnvConfig()
    return config

@pytest.mark.parametrize("env_value, expected_value", [("test_value", "test_value"), (None, None)])
def test_EnvConfig_init(env_value, expected_value, mock_env_config):
    """Test initialization of EnvConfig.
    
    Tests if the EnvConfig is correctly initialized with environment variables.
    
    Args:
        env_value (str or None): Mock environment variable value
        expected_value (str or None): Expected value for EnvConfig attributes
        mock_env_config (EnvConfig): Mocked environment configuration
    """
    assert mock_env_config.openai_key == expected_value
    assert mock_env_config.pinecone_key == expected_value

@pytest.mark.asyncio
@pytest.mark.parallel
async def test_OpenAIHandler_create_embedding(mock_env_config):
    """Asynchronous test for creating embeddings via OpenAIHandler.
    
    Tests if OpenAIHandler.create_embedding method correctly returns mock response.
    
    Args:
        mock_env_config (EnvConfig): Mocked environment configuration
    """
    handler = OpenAIHandler(mock_env_config)
    mock_response = {"id": 1, "values": [0.1, 0.2, 0.3]}
    
    with patch.object(handler.openai.Embedding, 'create', return_value=mock_response):
        response = await handler.create_embedding("test_text")
        
    assert response == mock_response

@pytest.mark.parallel
def test_PineconeHandler_init(mock_env_config):
    """Test initialization of PineconeHandler.
    
    Tests if PineconeHandler is correctly initialized with environment variables.
    
    Args:
        mock_env_config (EnvConfig): Mocked environment configuration
    """
    handler = PineconeHandler(mock_env_config)
    handler.pinecone.init.assert_called_with(api_key="test_value", environment="test_value")
    assert handler.index_name == "test_value"

@pytest.mark.asyncio
@pytest.mark.parallel
async def test_PineconeHandler_upload_embedding(mock_env_config):
    """Asynchronous test for uploading embeddings via PineconeHandler.
    
    Tests if PineconeHandler.upload_embedding method correctly calls pinecone.Index.upsert.
    
    Args:
        mock_env_config (EnvConfig): Mocked environment configuration
    """
    handler = PineconeHandler(mock_env_config)
    mock_embedding = {
        "id": "1",
        "values": [0.1, 0.2, 0.3],
        "metadata": {},
        "sparse_values": {}
    }
    
    with patch.object(handler.pinecone.Index, 'upsert', return_value=None):
        await handler.upload_embedding(mock_embedding)
        
    handler.pinecone.Index.assert_called_with("test_value")

@pytest.mark.asyncio
@pytest.mark.parallel
async def test_DataStreamHandler_process_data(mock_env_config):
    """Asynchronous test for processing data via DataStreamHandler.
    
    Tests if DataStreamHandler.process_data method correctly calls methods of OpenAIHandler and PineconeHandler.
    
    Args:
        mock_env_config (EnvConfig): Mocked environment configuration
    """
    openai_handler = OpenAIHandler(mock_env_config)
    pinecone_handler = PineconeHandler(mock_env_config)
    handler = DataStreamHandler(openai_handler, pinecone_handler)
    
    mock_data = "test_data"
    mock_embedding = {"id": 1, "values": [0.1, 0.2, 0.3]}
    
    with patch.object(OpenAIHandler, 'create_embedding', return_value=mock_embedding):
        with patch.object(PineconeHandler, 'upload_embedding', return_value=None):
            await handler.process_data(mock_data)
