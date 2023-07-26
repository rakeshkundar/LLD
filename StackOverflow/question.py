from __future__ import annotations
from datetime import datetime
from system_enums import QuestionStatus, QuestionClosingRemark
from bounty import Bounty
from accounts.member import Member
from photo import Photo
from comment import Comment
from answer import Answer


class Question:
    id: str
    title: str
    description: str
    view_count: int
    vote_count: int
    creation_time: datetime
    updated_time: datetime
    status: QuestionStatus
    closing_remark: QuestionClosingRemark
    bounty: Bounty
    asked_by: Member
    photos: list(Photo)
    comments: list(Comment)
    answers: list(Answer)

    def __init__(self, id: str, title: str, desc: str, view_count: int, vote_count: int, asked_by: Member, bounty: Bounty) -> None:
        self.id = id
        self.title = title
        self.description = desc
        self.view_count = view_count
        self.vote_count = vote_count
        self.creation_time = datetime.now()
        self.updated_time = datetime.now()
        self.status = QuestionStatus.OPEN
        self.closing_remark = None
        self.bounty = bounty
        self.photos = []
        self.answers = []
        self.comments = []


    def close(self):
        pass

    def undelete(self):
        pass

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_bounty(self, bounty):
        self.bounty = bounty