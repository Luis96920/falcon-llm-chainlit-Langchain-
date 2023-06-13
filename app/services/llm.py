from langchain import HuggingFaceHub

from app.helper.logger_formatter import CustomLogger


class GenericLLM:
    def __init__(self, name: str, temperature: float = 0.0, max_new_tokens: int = 1000):
        self.logger = CustomLogger.build("LLM")
        self.name = name
        self.temperature = temperature
        self.max_new_tokens = max_new_tokens
        self.logger.info(f"loading {self.name} model")

    def get_llm(self) -> HuggingFaceHub:
        pass


class FalconLLM(GenericLLM):
    def __init__(
        self,
        name: str,
        repo_id: str,
        hf_api_token: str,
        temperature: float = 0.1,
        max_new_tokens: int = 1000,
    ):
        super().__init__(name, temperature, max_new_tokens)
        self.repo_id = repo_id
        self.hf_api_token = hf_api_token

    def get_llm(self):
        return HuggingFaceHub(
            huggingfacehub_api_token=self.hf_api_token,
            repo_id=self.repo_id,
            model_kwargs={
                "temperature": self.temperature,
                "max_new_tokens": self.max_new_tokens,
            },
        )
