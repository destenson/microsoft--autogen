from typing import Union

from ..agent import Agent, AgentStream
from ..chat_summarizers.last_message import LastMessageSummarizer
from ..speaker_selections.round_robin_speaker_selection import RoundRobin
from ..summarizer import ChatSummarizer
from ..termination import Termination
from ..terminations.default_termination import DefaultTermination
from .group_chat import GroupChat


class TwoAgentChat(GroupChat):
    def __init__(
        self,
        first: Union[Agent, AgentStream],
        second: Union[Agent, AgentStream],
        *,
        termination_manager: Termination = DefaultTermination(),
        summarizer: ChatSummarizer = LastMessageSummarizer()
    ):
        super().__init__(
            agents=[first, second],
            speaker_selection=RoundRobin(),
            termination_manager=termination_manager,
            summarizer=summarizer,
            send_introduction=False,
        )
